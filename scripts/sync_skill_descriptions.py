import os
import re
from pathlib import Path


REPO = Path(__file__).resolve().parents[1]
REPO_SKILLS = REPO / "skills"
LOCAL_SKILLS = Path(os.environ.get("CODEX_SKILLS_DIR", Path.home() / ".codex" / "skills"))


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def parse_frontmatter(text: str) -> tuple[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", text, re.S)
    if not match:
        return "", text
    return match.group(1), text[match.end():]


def field(frontmatter: str, name: str) -> str:
    match = re.search(rf"(?m)^{re.escape(name)}:\s*(.+?)\s*$", frontmatter)
    return match.group(1).strip().strip('"').strip("'") if match else ""


def replace_description(frontmatter: str, description: str) -> str:
    escaped = description.replace('"', r"\"")
    line = f'description: "{escaped}"'
    if re.search(r"(?m)^description:\s*", frontmatter):
        frontmatter = re.sub(
            r"(?ms)^description:\s*(?:\|[^\n]*(?:\n(?:\s+.*|\s*$))*)?.*?(?=^[A-Za-z0-9_-]+:|\Z)",
            line + "\n",
            frontmatter,
            count=1,
        ).rstrip()
    else:
        frontmatter = frontmatter.rstrip() + "\n" + line
    return frontmatter


def main() -> int:
    if not LOCAL_SKILLS.exists():
        print(f"local skills directory not found: {LOCAL_SKILLS}")
        print("Set CODEX_SKILLS_DIR to the directory that contains local Codex skill folders.")
        return 0

    local_by_folder = {}
    for path in LOCAL_SKILLS.rglob("SKILL.md"):
        local_by_folder[path.parent.name] = path

    updated = []
    skipped = []
    for repo_path in REPO_SKILLS.rglob("SKILL.md"):
        local_path = local_by_folder.get(repo_path.parent.name)
        if not local_path:
            skipped.append(str(repo_path.relative_to(REPO)))
            continue
        local_fm, _ = parse_frontmatter(read(local_path))
        repo_fm, repo_body = parse_frontmatter(read(repo_path))
        local_desc = field(local_fm, "description")
        if not local_desc:
            skipped.append(str(repo_path.relative_to(REPO)))
            continue
        if field(repo_fm, "description") == local_desc:
            continue
        new_fm = replace_description(repo_fm, local_desc)
        repo_path.write_text("---\n" + new_fm + "\n---\n\n" + repo_body.lstrip(), encoding="utf-8")
        updated.append(str(repo_path.relative_to(REPO)))

    print(f"updated={len(updated)}")
    print(f"skipped={len(skipped)}")
    for item in updated:
        print(item)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
