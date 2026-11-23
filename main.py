"""Real-Life Patch Notes: The Comedy Changelog.

Writes a single original patch-note line about a bug in human
biology to <MAKEFUN_OUTPUT_DIR or /output>/entry.txt.

Deterministic: the same line is written on every run. Stdlib only,
no network, no file reads outside this repo.
"""

import os

# One original line, invented for this entry. A software-style patch
# note for a bug in real life: the stomach's impeccable timing.
LINE = (
    "v1.9.3: fixed a bug where the stomach growled loudest during "
    "the quietest moment of a silent exam hall."
)

MAX_CHARS = 160


def validate(line: str) -> None:
    """Enforce the competition gate: 1-160 chars, single line, not blank."""
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line (no newline characters)")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    # The file must hold exactly this line as UTF-8, nothing else.
    line.encode("utf-8")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    # No trailing newline: the file holds exactly the single line.
    with open(path, "wb") as f:
        f.write(data)
    # Round-trip check: what is on disk must be exactly what we wrote.
    with open(path, "rb") as f:
        if f.read() != data:
            raise RuntimeError("entry.txt round-trip mismatch")
    print(f"wrote {len(data)} bytes ({len(LINE)} characters) to {path}")


if __name__ == "__main__":
    main()
