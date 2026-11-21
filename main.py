"""make.fun news-image-20261120 entrypoint.

Copies the pre-rendered front-page poster (entry.png, drawn in this
repository from news researched for Friday 20 November 2026) to the
grader output directory. Standard library only; no network.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    # Copy byte-for-byte so both grader runs produce identical output.
    # The poster itself is deterministic: render.py draws it from
    # stories.py with a fixed-seed grain, so re-rendering reproduces
    # the same bytes as well.
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
