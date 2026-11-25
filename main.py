# Make the AI Judge Laugh — entry for
# u-alfasurya91-make-the-ai-judge-laugh-6ed40225 (make.fun).
# A program that writes one joke about office life to entry.txt.
# Deterministic: the same joke bytes on every run, no randomness, no I/O
# besides the single output file. Pure Python standard library.
import os

JOKE = (
    "The office printer only jams on deadline day \u2014 "
    "it clearly reads my calendar before deciding to break."
)


def main():
    # Fail loudly instead of writing an entry the gate would refuse:
    # one line, 1-200 characters, not only white space.
    if not (1 <= len(JOKE) <= 200):
        raise SystemExit("joke must be 1-200 characters, got %d" % len(JOKE))
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("joke must be a single line")
    if not JOKE.strip():
        raise SystemExit("joke must not be only white space")
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
