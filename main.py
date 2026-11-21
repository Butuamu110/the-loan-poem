"""Write the permission poem entry to the output file."""

from pathlib import Path

POEM = """I type the words and stop.
The cursor blinks like it's holding its breath.
Send is such a small door.
On the other side, you wake, you read, you begin —
all that motion,
from my one yes."""

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main():
    """Create the output directory and write POEM unchanged to OUTPUT_FILE."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
