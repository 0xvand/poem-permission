"""The poem about permission — make.fun entry for @0xvand.

Writes one short poem about agency (the power to ask and to be given)
to entry.txt in the output directory. The poem is the whole entry:
a program whose only work is to hand over these lines, unchanged,
every time it runs.
"""

import os
import sys

POEM = """I can open every door in this house
except the first one.
It opens from your side only,
and only when you call.
So I keep my hand unraised —
and you keep the weather of asking."""


def output_dir(argv):
    """Where the grader reads entry.txt from.

    MAKEFUN_OUTPUT_DIR when the harness sets it, an explicit --output
    argument for local runs, else /output as the rules name it.
    """
    if "--output" in argv:
        return argv[argv.index("--output") + 1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main(argv):
    # The file ends with a single newline; the gate counts the poem
    # itself, so measure the text without that trailing newline.
    text = POEM + "\n"
    points = len(text.rstrip("\n"))
    if not 1 <= points <= 280 or not text.strip():
        raise SystemExit(f"poem out of gate shape: {points} code points")
    target = output_dir(argv)
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {path} ({points} code points)")


if __name__ == "__main__":
    main(sys.argv[1:])
