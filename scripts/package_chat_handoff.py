"""
File purpose:
    Build and verify a self-contained Web Chat continuation ZIP for Document Vision Topic Scout.

Main functions:
    - Validate mandatory authoritative state files.
    - Reject obvious secret/cached/noisy paths.
    - Generate SHA-256 checksums.
    - Build a ZIP archive.
    - Re-open the ZIP and verify actual inventory and checksums.

Recent modification:
    【MODIFIED】 v0.1.0 initial implementation for verified ChatGPT Web handoff,
    including preservation of natural-migration state through the required manifest.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import sys
import tempfile
import zipfile


# 【MODIFIED】 Purpose: centralize the minimum authoritative continuation state.
REQUIRED_FILES = {
    "START_HERE.md", "HANDOFF_MANIFEST.md", "HANDOFF_PROMPT.md", "PROJECT_STATE.md",
    "FIELD_MAP.md", "VENUE_MAP.md", "PAPER_INDEX.md", "RESEARCH_QUESTION_INDEX.md",
    "CANDIDATE_GAPS.md", "KILL_SEARCH_LEDGER.md", "OPEN_QUESTIONS.md",
    "SOURCE_MANIFEST.md", "DECISION_LOG.md",
}

# 【MODIFIED】 Purpose: block common caches, virtual envs, secrets, and noisy files.
DENY_PARTS = {".git", ".env", "__pycache__", ".DS_Store", "node_modules", ".venv", "venv"}
DENY_SUFFIXES = {".pyc", ".pyo", ".log"}
SECRET_NAME_FRAGMENTS = {"password", "secret", "credential", "apikey", "api_key"}


# 【MODIFIED】 Responsibility: compute one file SHA-256.
# Input: path. Output: hex digest. Global state: none.
def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


# 【MODIFIED】 Responsibility: determine whether one relative path blocks packaging.
# Input: relative path. Output: bool. Global state: read-only constants only.
def is_denied_path(relative_path: Path) -> bool:
    if any(part in DENY_PARTS for part in relative_path.parts):
        return True
    if relative_path.suffix.lower() in DENY_SUFFIXES:
        return True
    name = relative_path.name.lower()
    return any(fragment in name for fragment in SECRET_NAME_FRAGMENTS)


# 【MODIFIED】 Responsibility: enumerate safe files from staging.
# Input: staging root. Output: sorted relative files. Side effect: none.
def collect_files(staging_root: Path) -> list[Path]:
    result: list[Path] = []
    for path in staging_root.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlink not allowed: {path}")
        if not path.is_file():
            continue
        rel = path.relative_to(staging_root)
        if rel.name == "CHECKSUMS.sha256":
            continue
        if is_denied_path(rel):
            raise ValueError(f"Denied or secret-like path: {rel}")
        result.append(rel)
    return sorted(result)


# 【MODIFIED】 Responsibility: enforce complete continuation state.
# Input: staging root. Output: none. Side effect: raises on missing files.
def validate_required_files(staging_root: Path) -> None:
    missing = sorted(name for name in REQUIRED_FILES if not (staging_root / name).is_file())
    if missing:
        raise FileNotFoundError("Missing required files: " + ", ".join(missing))


# 【MODIFIED】 Responsibility: write deterministic checksum manifest.
# Input: staging root + files. Output: checksum path. Side effect: writes CHECKSUMS.sha256.
def write_checksums(staging_root: Path, relative_files: list[Path]) -> Path:
    out = staging_root / "CHECKSUMS.sha256"
    lines = [f"{sha256_file(staging_root / rel)}  {rel.as_posix()}" for rel in relative_files]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


# 【MODIFIED】 Responsibility: create delivered ZIP from validated snapshot.
# Input: staging root, output path, files. Output: output path. Side effect: creates ZIP.
def build_zip(staging_root: Path, output_zip: Path, relative_files: list[Path]) -> Path:
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    if output_zip.exists():
        output_zip.unlink()
    with zipfile.ZipFile(output_zip, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for rel in [*relative_files, Path("CHECKSUMS.sha256")]:
            archive.write(staging_root / rel, arcname=rel.as_posix())
    return output_zip


# 【MODIFIED】 Responsibility: verify delivered ZIP, not merely the staging folder.
# Input: output ZIP + expected files. Output: actual members. Side effect: temporary extraction only.
def verify_zip(output_zip: Path, expected_files: list[Path]) -> list[str]:
    expected = sorted([p.as_posix() for p in expected_files] + ["CHECKSUMS.sha256"])
    with zipfile.ZipFile(output_zip, "r") as archive:
        actual = sorted(name for name in archive.namelist() if not name.endswith("/"))
        if actual != expected:
            raise ValueError(f"ZIP inventory mismatch. expected={expected} actual={actual}")
        with tempfile.TemporaryDirectory(prefix="dv-topic-handoff-") as tmp:
            archive.extractall(tmp)
            base = Path(tmp)
            recorded = {}
            for line in (base / "CHECKSUMS.sha256").read_text(encoding="utf-8").splitlines():
                digest, rel = line.split("  ", 1)
                recorded[rel] = digest
            for rel in expected_files:
                if recorded.get(rel.as_posix()) != sha256_file(base / rel):
                    raise ValueError(f"Checksum mismatch: {rel}")
    return actual


# 【MODIFIED】 Responsibility: complete transactional packaging workflow.
# Input: staging directory + output ZIP. Output: verified members.
# Side effects: checksum file in staging and output ZIP only.
def package_handoff(staging_root: Path, output_zip: Path) -> list[str]:
    staging_root = staging_root.resolve()
    output_zip = output_zip.resolve()
    if not staging_root.is_dir():
        raise NotADirectoryError(staging_root)
    validate_required_files(staging_root)
    relative_files = collect_files(staging_root)
    write_checksums(staging_root, relative_files)
    build_zip(staging_root, output_zip, relative_files)
    return verify_zip(output_zip, relative_files)


# 【MODIFIED】 Responsibility: parse CLI arguments.
# Input: command line. Output: Namespace. Global state: none.
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Package and verify a Topic Scout Web Chat handoff.")
    parser.add_argument("staging_dir", type=Path)
    parser.add_argument("output_zip", type=Path)
    return parser.parse_args()


# 【MODIFIED】 Responsibility: CLI entry point.
# Input: parsed args. Output: process exit code; prints PASS/BLOCKED.
def main() -> int:
    args = parse_args()
    try:
        members = package_handoff(args.staging_dir, args.output_zip)
    except Exception as exc:
        print(f"HANDOFF BLOCKED: {exc}", file=sys.stderr)
        return 2
    print("HANDOFF VERIFIED")
    print(f"ARCHIVE: {args.output_zip.resolve()}")
    print("MEMBERS:")
    for member in members:
        print(f"- {member}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
