"""Entry for make.fun's "The poem about stopping".

Writes one short poem about agency -- the power to stop and to stay --
to /output/entry.txt. A guide dog refuses a crossing and holds her
person still until the world is safe to bear his weight.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

POEM = """The crossing clicks: go, go.
His hand asks through the harness.
The dog plants all four feet.
A truck blows rain across his shoes.
He waits for her to tell him
when the world can hold his weight."""


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
