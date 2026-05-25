import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "catalog"
ROOTS = [
    ("repo-skills", WORKSPACE / "skills"),
    ("user-local", Path(r"C:\Users\LENOVO\.codex\skills")),
    ("plugin-cache", Path(r"C:\Users\LENOVO\.codex\plugins\cache")),
]


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
        "path": str(skill_path),
        "repo_path": rel if str(skill_path).startswith(str(WORKSPACE)) else "",
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

    readme = [
        "# Codex Skills Natural-Language Database",
        "",
        "This private repository indexes local Codex skills so an assistant can route natural-language requests to the right skill without requiring the user to remember skill names.",
        "",
        "## Files",
        "",
        "- `catalog/skills.json`: full structured database.",
        "- `catalog/preferred-skills.json`: de-duplicated best source per skill name.",
        "- `catalog/skills.jsonl`: one skill per line for ingestion.",
        "- `catalog/skills.csv`: spreadsheet-friendly inventory.",
        "- `catalog/skills.sqlite`: SQLite database with FTS5 full-text search.",
        "- `catalog/keyword_index.json`: keyword to skill-id inverted index.",
        "- `catalog/category_index.md`: human-readable category map.",
        "- `docs/skill-routing-policy.md`: routing policy and tie breakers.",
        "- `scripts/query_skills.py`: local natural-language query helper.",
        "",
        "## Query Example",
        "",
        "```powershell",
        "& 'C:\\Users\\LENOVO\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\python\\python.exe' scripts\\query_skills.py '报错 跑不起来 帮我排查'",
        "```",
        "",
        "## Design",
        "",
        "The database is trigger-first: descriptions and search fields describe when to use a skill, not the workflow inside the skill. Chinese trigger phrases are included for common local usage.",
        "",
    ]
    existing = (OUT.parent / "README.md").read_text(encoding="utf-8", errors="replace") if (OUT.parent / "README.md").exists() else ""
    if "## Natural-Language Skill Routing" not in existing:
        existing = existing.rstrip() + "\n\n## Natural-Language Skill Routing\n\n" + "\n".join(readme[2:]) + "\n"
        (OUT.parent / "README.md").write_text(existing, encoding="utf-8")

    routing = [
        "# Skill Routing Policy",
        "",
        "## Decision Order",
        "",
        "1. Match the user request against category, description, keywords, and Chinese trigger phrases.",
        "2. Prefer process skills first when the request involves planning, debugging, implementation, review, or verification.",
        "3. Then select the most specific domain skill for the tool, file type, framework, or output.",
        "4. If multiple skills tie, choose the narrower skill with the strongest exact keyword overlap.",
        "5. If no skill scores well, proceed normally and record the missing trigger as a future improvement.",
        "",
        "## High-Signal Chinese Triggers",
        "",
    ]
    for cat, phrases in ZH_TRIGGERS.items():
        routing.append(f"- `{cat}`: " + ", ".join(phrases))
    routing.append("")
    (OUT.parent / "docs").mkdir(exist_ok=True)
    (OUT.parent / "docs" / "skill-routing-policy.md").write_text("\n".join(routing), encoding="utf-8")

    scripts = OUT.parent / "scripts"
    scripts.mkdir(exist_ok=True)
    query_script = r'''import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "catalog" / "skills.sqlite"
JSON_DB = ROOT / "catalog" / "skills.json"

def quote_terms(query: str) -> str:
    terms = [t.strip() for t in query.replace("/", " ").replace("\\", " ").split() if t.strip()]
    if not terms:
        return ""
    return " OR ".join('"' + t.replace('"', '""') + '"' for t in terms)

def main() -> int:
    query = " ".join(sys.argv[1:]).strip()
    if not query:
        print("Usage: query_skills.py <natural language request>")
        return 2
    match = quote_terms(query)
    combined = {}
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    if match:
        try:
            rows = con.execute(
                """
                SELECT s.id, s.name, s.category, s.description, s.source_package, s.path, bm25(skills_fts) AS score
                FROM skills_fts
                JOIN skills s ON s.rowid = skills_fts.rowid
                WHERE skills_fts MATCH ?
                ORDER BY score
                LIMIT 25
                """,
                (match,),
            ).fetchall()
            for row in rows:
                combined[row["id"]] = {
                    "name": row["name"],
                    "category": row["category"],
                    "description": row["description"],
                    "source_package": row["source_package"],
                    "path": row["path"],
                    "score": float(row["score"]),
                    "reason": "fts",
                }
        except sqlite3.OperationalError:
            pass

    data = json.loads(JSON_DB.read_text(encoding="utf-8"))
    raw_terms = [t.lower() for t in re.findall(r"[\u4e00-\u9fffA-Za-z0-9.+#/_-]{2,}", query)]
    chars = set(ch for ch in query if "\u4e00" <= ch <= "\u9fff")
    for r in data["skills"]:
        haystack = " ".join([
            r["name"],
            r["category"],
            r["description"],
            " ".join(r.get("keywords", [])),
            " ".join(r.get("trigger_phrases", [])),
            " ".join(r.get("zh_triggers", [])),
            r.get("search_text", ""),
        ]).lower()
        score = 0.0
        hits = []
        for term in raw_terms:
            if term in haystack:
                score += 8.0 if any("\u4e00" <= ch <= "\u9fff" for ch in term) else 4.0
                hits.append(term)
        for phrase in r.get("trigger_phrases", []):
            if phrase and phrase in query:
                score += 25.0
                hits.append(phrase)
        for phrase in r.get("zh_triggers", []):
            if phrase and phrase in query:
                score += 6.0
                hits.append(phrase)
        keyword_chars = set()
        for phrase in r.get("trigger_phrases", []) + r.get("zh_triggers", []) + r.get("keywords", []):
            keyword_chars.update(ch for ch in phrase if "\u4e00" <= ch <= "\u9fff")
        overlap = len(chars & keyword_chars)
        if overlap:
            score += min(overlap, 12) * 0.6
        if r["name"] == "website-to-hyperframes" and any(x in query for x in ["网址", "网站", "网页", "链接", "URL", "url"]):
            score += 35.0
        if r["name"] == "hyperframes-media" and any(x in query for x in ["字幕", "配音", "转录", "语音", "背景移除"]):
            score += 18.0
        if r["name"] == "hyperframes" and any(x in query for x in ["视频", "动画", "合成"]):
            score += 10.0
        if score > 0:
            existing = combined.get(r["id"])
            normalized = -score
            if existing:
                existing["score"] += normalized
                existing["reason"] += "+keyword"
            else:
                combined[r["id"]] = {
                    "name": r["name"],
                    "category": r["category"],
                    "description": r["description"],
                    "source_package": r["source_package"],
                    "path": r["path"],
                    "score": normalized,
                    "reason": "keyword",
                }

    source_priority = {"repository": 0, ".system": 1, "local": 2, "hyperframes": 3, "openai-developers": 4, "figma": 5}
    sorted_rows = sorted(combined.values(), key=lambda x: (x["score"], source_priority.get(x["source_package"], 9)))
    deduped = []
    seen_names = set()
    for row in sorted_rows:
        if row["name"] in seen_names:
            continue
        seen_names.add(row["name"])
        deduped.append(row)
        if len(deduped) >= 10:
            break
    rows = deduped
    if not rows:
        rows = con.execute(
            """
            SELECT name, category, description, source_package, path, 999 AS score
            FROM skills
            WHERE search_text LIKE ?
            LIMIT 10
            """,
            ("%" + query + "%",),
        ).fetchall()
    for i, row in enumerate(rows, 1):
        print(f"{i}. {row['name']} [{row['category']}] score={row['score']} reason={row.get('reason', 'sql') if hasattr(row, 'get') else 'sql'}")
        print(f"   {row['description']}")
        print(f"   source={row['source_package']}")
        print(f"   path={row['path']}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'''
    (scripts / "query_skills.py").write_text(query_script, encoding="utf-8")

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
