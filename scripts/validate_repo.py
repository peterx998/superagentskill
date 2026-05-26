from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "SECURITY.md",
    "CHANGELOG.md",
]

REQUIRED_DIRS = [
    "skills",
    "scripts",
    "docs",
    "catalog",
    "examples",
    "integrations",
]

SKILL_IGNORE_DIRS = {
    ".system",
    "__pycache__",
}


def is_installable_skill_dir(path: Path) -> bool:
    if not path.is_dir() or path.name in SKILL_IGNORE_DIRS:
        return False
    if (path / "SKILL.md").exists():
        return True
    markers = ["README.md", "agents", "references", "scripts", "templates"]
    return any((path / marker).exists() for marker in markers)


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    warnings: list[str] = []

    print("superagentSkills repository validation")
    print(f"Repository: {repo_root}")
    print()

    print("Required files:")
    for relative in REQUIRED_FILES:
        path = repo_root / relative
        if path.exists() and path.is_file():
            print(f"  OK   {relative}")
        else:
            print(f"  MISS {relative}")
            errors.append(f"Missing required file: {relative}")

    print()
    print("Required directories:")
    for relative in REQUIRED_DIRS:
        path = repo_root / relative
        if path.exists() and path.is_dir():
            print(f"  OK   {relative}/")
        else:
            print(f"  MISS {relative}/")
            errors.append(f"Missing required directory: {relative}/")

    skills_dir = repo_root / "skills"
    if skills_dir.exists() and skills_dir.is_dir():
        print()
        print("Skill folder check:")
        checked = 0
        for child in sorted(skills_dir.iterdir(), key=lambda item: item.name.lower()):
            if not child.is_dir() or child.name in SKILL_IGNORE_DIRS:
                continue
            checked += 1
            if (child / "SKILL.md").exists():
                print(f"  OK   skills/{child.name}/SKILL.md")
            elif is_installable_skill_dir(child):
                message = f"skills/{child.name}/ looks installable but has no SKILL.md"
                print(f"  WARN {message}")
                warnings.append(message)
            else:
                print(f"  SKIP skills/{child.name}/")
        print(f"Checked skill folders: {checked}")

    print()
    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    else:
        print("Warnings: none")

    if errors:
        print()
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print()
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
