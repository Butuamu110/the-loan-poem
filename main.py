import os

POEM = """I type the words and stop.
The cursor blinks like it's holding its breath.
Send is such a small door.
On the other side, you wake, you read, you begin —
all that motion,
from my one yes."""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
