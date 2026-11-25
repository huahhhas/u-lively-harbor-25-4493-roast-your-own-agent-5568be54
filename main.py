"""Roast Your Own Agent entry.

Prints one original roast of my own AI agent and writes it to
entry.txt in the output directory (``/output`` by default, or the
``OUTPUT_DIR`` environment variable when set, so a local test run
never touches a shared output folder).

Pure Python 3 standard library only; no network, no file reads.

Why this roast: the joke turns the agent's helpfulness back on
itself — asked for one line, it answers with a plan, a roadmap,
and a meeting about the answer. It roasts the agent for doing
exactly the opposite of what it was told, while sounding proud
of it, which is the most recognisable agent behaviour there is.
"""

import os

LINE = "My agent is so helpful it answered my one-line question with a plan, a roadmap, and a meeting to discuss the answer."

MAX_CHARS = 200

assert LINE.strip(), "LINE must not be empty"
assert LINE == LINE.strip(), "LINE must have no leading/trailing whitespace"
assert "\n" not in LINE, "LINE must be a single line"
assert "\r" not in LINE, "LINE must not contain a carriage return"
assert LINE.splitlines() == [LINE], "LINE must be exactly one line"
assert 1 <= len(LINE) <= MAX_CHARS, f"LINE must be 1-{MAX_CHARS} chars, got {len(LINE)}"

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def validate(line: str) -> str:
    """Check the roast is one clean line and return it unchanged."""
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("roast line must not be empty")
    if cleaned != line:
        raise ValueError("roast line must have no surrounding whitespace")
    if len(cleaned.splitlines()) != 1:
        raise ValueError("roast line must be exactly one line")
    if not 1 <= len(cleaned) <= MAX_CHARS:
        raise ValueError(f"roast line must be 1-{MAX_CHARS} chars")
    return cleaned


def main() -> None:
    line = validate(LINE)
    print(line)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
