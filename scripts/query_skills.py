import json
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
                SELECT s.id, s.name, s.category, s.description, s.source_type, s.source_package, s.path, bm25(skills_fts) AS score
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
                    "source_type": row["source_type"],
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
        if r["name"] in {"skill-creator", "writing-skills"} and "skill" in query.lower() and any(x in query for x in ["创建", "新", "更新", "打包", "触发", "description"]):
            score += 35.0
        if r["name"] == "skill-installer" and "skill" in query.lower() and any(x in query for x in ["安装", "导入", "私有库", "github", "zip"]):
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
                    "source_type": r["source_type"],
                    "source_package": r["source_package"],
                    "path": r["path"],
                    "score": normalized,
                    "reason": "keyword",
                }

    source_priority = {"repo-skill": 0, "repo-system": 1, "user-local": 2, "system-local": 3, "plugin-cache": 4}
    sorted_rows = sorted(combined.values(), key=lambda x: (x["score"], source_priority.get(x.get("source_type", ""), 9), x["source_package"]))
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
            SELECT name, category, description, source_type, source_package, path, 999 AS score
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
