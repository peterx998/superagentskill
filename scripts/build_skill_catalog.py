import csv
import hashlib
import json
import os
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "catalog"
ROOTS = [("repo-skills", WORKSPACE / "skills")]

if os.environ.get("SUPERAGENTSKILLS_INCLUDE_LOCAL") == "1":
    local_home = Path.home()
    ROOTS.extend(
        [
            ("user-local", local_home / ".codex" / "skills"),
            ("plugin-cache", local_home / ".codex" / "plugins" / "cache"),
        ]
    )


CATEGORY_RULES = [
    ("routing-process", ["route", "skill", "conversation", "brainstorm", "plan", "implementation plan", "execute", "parallel", "worktree", "branch", "approval", "gate"]),
    ("debugging-code-quality", ["debug", "bug", "fix", "test", "review", "verify", "complete", "passing", "refactor", "karpathy", "ci", "failure", "error", "crash", "flaky"]),
    ("skill-authoring-local-diagnostics", ["skill.md", "skills", "local diagnostics", "workspace", "runtime", "whoami", "scan", "package", "install"]),
    ("agent-security-runtime", ["agent", "runtime", "mcp", "prompt injection", "policy", "security", "tool-call", "shell hook", "repo poisoning", "lab"]),
    ("content-knowledge-marketing", ["hook", "ugc", "ad", "seo", "geo", "obsidian", "knowledge", "wiki", "notes", "marketing", "copy"]),
    ("hyperframes-video", ["hyperframes", "video", "caption", "subtitle", "voiceover", "tts", "transcribe", "registry", "remotion", "website-to-video", "promo"]),
    ("animation-rendering", ["gsap", "animation", "three", "webgl", "webgpu", "shader", "lottie", "anime", "waapi", "tailwind", "css keyframes", "canvas"]),
    ("documents-data-presentations", ["spreadsheet", "document", "docx", "presentation", "slides", "powerpoint", "canva", "figma"]),
    ("github-project-workflows", ["github", "pull request", "issue", "commit", "push", "repo", "repository", "actions"]),
    ("openai-api-apps", ["openai", "api key", "agents sdk", "chatgpt app", "mcp server", "model", "eval"]),
]


ZH_TRIGGERS = {
    "routing-process": ["规划", "计划", "先想方案", "设计一下", "按计划执行", "拆任务", "并行处理", "新功能", "改行为"],
    "debugging-code-quality": ["报错", "修复", "排查", "跑不起来", "失败", "崩溃", "卡住", "测试失败", "代码审查", "验收"],
    "skill-authoring-local-diagnostics": ["创建技能", "修改技能", "技能触发", "本地诊断", "扫描目录", "运行环境", "技能打包"],
    "agent-security-runtime": ["MCP安全", "提示注入", "代理运行时", "工具调用", "策略检查", "安全审计"],
    "content-knowledge-marketing": ["短视频hook", "广告开头", "UGC脚本", "知识库", "双链笔记", "Obsidian", "SEO", "GEO"],
    "hyperframes-video": ["做视频", "字幕", "配音", "视频合成", "网页转视频", "网址做成视频", "链接做视频", "宣传片", "产品视频", "产品宣传视频"],
    "animation-rendering": ["动画", "滚动动画", "三维", "WebGL", "WebGPU", "粒子", "着色器", "动效"],
    "documents-data-presentations": ["表格", "文档", "PPT", "幻灯片", "演示文稿", "Figma", "Canva"],
    "github-project-workflows": ["上传GitHub", "私有库", "提交", "推送", "PR", "issue", "仓库"],
    "openai-api-apps": ["OpenAI接口", "API key", "智能体", "模型", "ChatGPT应用", "评测"],
}


EXTRA_TERMS = {
    "systematic-debugging": ["error", "exception", "stack trace", "logs", "root cause", "报错", "修复", "排查", "跑不起来"],
    "skill-router": ["choose skill", "route skill", "auto trigger", "natural language trigger", "技能路由", "自动触发"],
    "hook-skills": ["first 3 seconds", "viral hook", "TikTok", "Reels", "Shorts", "广告开头", "短视频hook"],
    "obsidian-llm-wiki-builder": ["vault", "backlinks", "evergreen notes", "知识库", "双链笔记"],
    "agent-runtime-lab": ["prompt injection", "MCP audit", "tool routing", "提示注入", "MCP安全"],
    "website-to-hyperframes": ["website to video", "turn site into video", "网页转视频", "网址做成视频", "网站做视频", "链接做视频", "产品宣传视频"],
    "skill-creator": ["create skill", "new skill", "创建skill", "创建技能", "更新skill", "技能打包"],
    "skill-installer": ["install skill", "import skill", "安装skill", "安装技能", "私有库skill", "zip安装"],
    "writing-skills": ["skill description", "trigger behavior", "SKILL.md", "技能触发", "触发描述"],
    "claude-typer": ["Claude typing animation", "prompt typing video", "提示词打字机", "Claude打字动画"],
    "light-spotlight-render": ["spotlight text reveal", "light logo reveal", "聚光灯扫字", "发光文字揭示"],
    "procedural-fish-render": ["procedural fish", "Remotion fish", "程序鱼", "程序鱼视频"],
    "remotion-3d-ticker": ["3D ticker", "vertical ticker", "photo wall", "3D照片滚动墙", "3D相册瀑布流"],
    "remotion-best-practices": ["Remotion", "video in React", "Remotion best practices", "Remotion视频"],
    "remotion-vinyl-player": ["vinyl player", "record player", "music player video", "黑胶唱片", "音乐播放器"],
    "ruler-progress-render": ["ruler progress", "progress animation", "尺子进度条", "尺子进度动画"],
    "svg-assembly-animator": ["SVG assembly", "transparent frame export", "SVG组装动画", "透明序列帧"],
    "threejs-earth-render": ["Three.js Earth", "globe route animation", "三维地球航线", "地球飞线"],
    "wechat-2d-render": ["WeChat 2D", "chat motion video", "微信聊天动画", "微信视频消息动效"],
}

FORCED_CATEGORY = {
    "skill-router": "routing-process",
    "using-superpowers": "routing-process",
    "skill-creator": "skill-authoring-local-diagnostics",
    "skill-installer": "skill-authoring-local-diagnostics",
    "plugin-creator": "skill-authoring-local-diagnostics",
    "animejs": "animation-rendering",
    "gsap-core": "animation-rendering",
    "gsap-frameworks": "animation-rendering",
    "gsap-scrolltrigger": "animation-rendering",
    "gsap-plugins": "animation-rendering",
    "gsap-react": "animation-rendering",
    "tailwind": "animation-rendering",
    "claude-typer": "hyperframes-video",
    "procedural-fish-render": "hyperframes-video",
    "remotion-3d-ticker": "hyperframes-video",
    "remotion-best-practices": "hyperframes-video",
    "remotion-vinyl-player": "hyperframes-video",
    "ruler-progress-render": "hyperframes-video",
    "wechat-2d-render": "hyperframes-video",
    "light-spotlight-render": "animation-rendering",
    "svg-assembly-animator": "animation-rendering",
    "threejs-earth-render": "animation-rendering",
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not match:
        return {}, text
    raw = match.group(1)
    body = text[match.end():]
    meta = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        simple = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not simple:
            i += 1
            continue
        key, value = simple.group(1), simple.group(2).strip()
        if value in {"|", ">"}:
            block = []
            i += 1
            while i < len(lines) and (lines[i].startswith(" ") or not re.match(r"^[A-Za-z0-9_-]+:", lines[i])):
                block.append(lines[i].strip())
                i += 1
            meta[key] = " ".join(x for x in block if x).strip()
            continue
        meta[key] = value.strip().strip('"').strip("'")
        i += 1
    return meta, body


def source_label(path: Path, root_kind: str) -> tuple[str, str]:
    if root_kind == "repo-skills":
        if "\\skills\\.system\\" in str(path).lower():
            return "repo-system", ".system"
        return "repo-skill", "repository"
    if root_kind == "user-local":
        if "\\.system\\" in str(path).lower():
            return "system-local", ".system"
        return "user-local", "local"
    parts = path.parts
    try:
        idx = parts.index("openai-curated")
        return "plugin-cache", parts[idx + 1] if idx + 1 < len(parts) else "openai-curated"
    except ValueError:
        pass
    try:
        idx = parts.index("openai-bundled")
        return "plugin-cache", "openai-bundled"
    except ValueError:
        pass
    try:
        idx = parts.index("openai-primary-runtime")
        return "plugin-cache", "openai-primary-runtime"
    except ValueError:
        pass
    return root_kind, "unknown"


def classify(name: str, description: str, body: str) -> tuple[str, list[str]]:
    if name in FORCED_CATEGORY:
        return FORCED_CATEGORY[name], [FORCED_CATEGORY[name]]
    haystack = f"{name} {description} {body[:2500]}".lower()
    scores = []
    for category, terms in CATEGORY_RULES:
        score = sum(1 for term in terms if term.lower() in haystack)
        if score:
            scores.append((score, category))
    scores.sort(reverse=True)
    category = scores[0][1] if scores else "uncategorized"
    tags = [cat for _, cat in scores[:3]]
    return category, tags


def extract_keywords(name: str, description: str, body: str, category: str) -> list[str]:
    text = f"{name} {description} {body[:5000]}"
    terms = set()
    for token in re.findall(r"[A-Za-z][A-Za-z0-9.+#/_-]{2,}", text):
        if len(token) <= 2:
            continue
        terms.add(token.lower())
    for phrase in re.findall(r"[\u4e00-\u9fffA-Za-z0-9.+#/_-]{2,}", description):
        if any("\u4e00" <= ch <= "\u9fff" for ch in phrase):
            terms.add(phrase)
    for phrase in ZH_TRIGGERS.get(category, []):
        terms.add(phrase)
    for phrase in EXTRA_TERMS.get(name, []):
        terms.add(phrase)
    stop = {"when", "with", "from", "that", "this", "into", "using", "user", "asks", "skill", "skills", "the", "and", "for"}
    return sorted(t for t in terms if t not in stop)[:90]


def make_record(skill_path: Path, root_kind: str) -> dict:
    text = read_text(skill_path)
    meta, body = parse_frontmatter(text)
    name = meta.get("name") or skill_path.parent.name
    description = meta.get("description", "")
    source_type, source_package = source_label(skill_path, root_kind)
    category, category_candidates = classify(name, description, body)
    keywords = extract_keywords(name, description, body, category)
    trigger_phrases = sorted(set(EXTRA_TERMS.get(name, [])))
    try:
        rel = str(skill_path.relative_to(WORKSPACE))
    except ValueError:
        rel = str(skill_path)
    record_id = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:12]
    headings = re.findall(r"(?m)^#{1,3}\s+(.+)$", body)
    search_text = " ".join([
        name,
        description,
        category,
        " ".join(category_candidates),
        " ".join(keywords),
        " ".join(trigger_phrases),
        " ".join(headings[:10]),
    ])
    if root_kind == "repo-skills":
        public_path = rel
        repo_path = rel
    elif root_kind == "user-local":
        public_path = f"<local-codex-skills>/{skill_path.parent.name}/SKILL.md"
        repo_path = ""
    elif root_kind == "plugin-cache":
        public_path = f"<plugin-cache>/{skill_path.parent.name}/SKILL.md"
        repo_path = ""
    else:
        public_path = ""
        repo_path = ""

    return {
        "id": record_id,
        "name": name,
        "folder": skill_path.parent.name,
        "category": category,
        "category_candidates": category_candidates,
        "description": description,
        "keywords": keywords,
        "trigger_phrases": trigger_phrases,
        "zh_triggers": ZH_TRIGGERS.get(category, []),
        "source_type": source_type,
        "source_package": source_package,
        "path": public_path,
        "repo_path": repo_path,
        "headings": headings[:12],
        "search_text": search_text,
    }


def write_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def build_sqlite(records: list[dict], path: Path) -> None:
    if path.exists():
        path.unlink()
    con = sqlite3.connect(path)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE skills (
            id TEXT PRIMARY KEY,
            name TEXT,
            folder TEXT,
            category TEXT,
            description TEXT,
            keywords TEXT,
            zh_triggers TEXT,
            source_type TEXT,
            source_package TEXT,
            path TEXT,
            search_text TEXT
        )
    """)
    cur.execute("CREATE VIRTUAL TABLE skills_fts USING fts5(name, category, description, keywords, zh_triggers, source_package, search_text, content='skills', content_rowid='rowid')")
    for r in records:
        cur.execute(
            "INSERT INTO skills VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                r["id"],
                r["name"],
                r["folder"],
                r["category"],
                r["description"],
                " ".join(r["keywords"]),
                " ".join(r["zh_triggers"] + r["trigger_phrases"]),
                r["source_type"],
                r["source_package"],
                r["path"],
                r["search_text"],
            ),
        )
    cur.execute("INSERT INTO skills_fts(skills_fts) VALUES('rebuild')")
    con.commit()
    con.close()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    seen_paths = set()
    for root_kind, root in ROOTS:
        if not root.exists():
            continue
        for path in sorted(root.rglob("SKILL.md")):
            if path in seen_paths:
                continue
            seen_paths.add(path)
            records.append(make_record(path, root_kind))

    source_rank = {"repo-skill": 0, "repo-system": 1, "user-local": 2, "system-local": 3, "plugin-cache": 4}
    records.sort(key=lambda r: (r["name"], source_rank.get(r["source_type"], 9), r["path"]))
    preferred = {}
    for r in records:
        preferred.setdefault(r["name"], r)
    preferred_records = sorted(preferred.values(), key=lambda r: (r["category"], r["name"]))
    records.sort(key=lambda r: (r["category"], r["name"], source_rank.get(r["source_type"], 9), r["path"]))
    by_category = defaultdict(list)
    for r in records:
        by_category[r["category"]].append(r)

    generated_at = datetime.now(timezone.utc).isoformat()
    summary = {
        "generated_at": generated_at,
        "total_skills": len(records),
        "unique_names": len(set(r["name"] for r in records)),
        "source_counts": Counter(r["source_type"] for r in records),
        "package_counts": Counter(r["source_package"] for r in records),
        "category_counts": Counter(r["category"] for r in records),
        "database_files": ["skills.json", "skills.jsonl", "skills.csv", "skills.sqlite", "keyword_index.json", "preferred-skills.json", "category_index.md"],
    }
    summary = json.loads(json.dumps(summary, ensure_ascii=False))

    write_json(OUT / "skills.json", {"summary": summary, "skills": records})
    write_json(OUT / "preferred-skills.json", {"summary": summary, "skills": preferred_records})
    with (OUT / "skills.jsonl").open("w", encoding="utf-8", newline="\n") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with (OUT / "skills.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "folder", "category", "description", "keywords", "trigger_phrases", "zh_triggers", "source_type", "source_package", "path"])
        writer.writeheader()
        for r in records:
            row = dict(r)
            row["keywords"] = "; ".join(r["keywords"])
            row["trigger_phrases"] = "; ".join(r["trigger_phrases"])
            row["zh_triggers"] = "; ".join(r["zh_triggers"])
            writer.writerow({k: row[k] for k in writer.fieldnames})

    keyword_index = defaultdict(list)
    for r in records:
        for term in r["keywords"] + r["zh_triggers"] + r["trigger_phrases"] + [r["category"], r["name"], r["folder"], r["source_package"]]:
            if term:
                keyword_index[term.lower()].append(r["id"])
    write_json(OUT / "keyword_index.json", dict(sorted(keyword_index.items())))
    build_sqlite(records, OUT / "skills.sqlite")

    md = [
        "# Superagent Skills Catalog",
        "",
        f"Generated: `{generated_at}`",
        f"Total records: `{summary['total_skills']}`",
        f"Unique skill names: `{summary['unique_names']}`",
        "",
        "## How Matching Works",
        "",
        "Use natural-language words from the user request against `description`, `keywords`, `zh_triggers`, `category`, and `search_text`.",
        "Prefer the narrowest high-score skill. If a process skill and a domain skill both match, use the process skill first, then the domain skill.",
        "",
        "SQLite FTS example:",
        "",
        "```sql",
        "SELECT s.name, s.category, s.description, bm25(skills_fts) AS score",
        "FROM skills_fts",
        "JOIN skills s ON s.rowid = skills_fts.rowid",
        "WHERE skills_fts MATCH '报错 OR 修复 OR debug'",
        "ORDER BY score",
        "LIMIT 8;",
        "```",
        "",
        "## Categories",
        "",
    ]
    for category in sorted(by_category):
        md.append(f"### {category}")
        md.append("")
        for r in by_category[category]:
            triggers = ", ".join(r["zh_triggers"][:6])
            md.append(f"- `{r['name']}` ({r['source_package']}): {r['description']}")
            if triggers:
                md.append(f"  - 中文触发: {triggers}")
        md.append("")
    (OUT / "category_index.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
