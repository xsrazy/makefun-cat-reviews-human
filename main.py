"""make.fun bounty entry: "Make the AI Judge Laugh: Cat Reviews Its Human".

Writes one line — a one-star review written by a house cat about the human
it lives with — to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Exactly the line's bytes, no trailing newline.
"""

LINE = "One star. He wakes me at 6 AM to feed me, then leaves for eight hours like the house runs itself. I brought him a mouse and he screamed. Would not recommend."

assert 1 <= len(LINE) <= 195 and LINE.strip(), "LINE must be 1-195 non-blank characters"
assert "\n" not in LINE, "LINE must be a single line"


def main() -> None:
    import os
    from pathlib import Path

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
