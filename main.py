"""One-line excuse entry: a gamer texts the boss a believable IT lockout.

Writes the single excuse line to entry.txt under $MAKEFUN_OUTPUT_DIR.
Stdlib only; no network, no secrets, no input files.
"""

import os

ENTRY = "Sorry, IT locked my account during the overnight update and they can't reimage my laptop till Friday."

def main():
    if not ENTRY.strip():
        raise ValueError("entry is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise RuntimeError(f"failed to write entry.txt: {exc}") from exc

if __name__ == "__main__":
    main()
