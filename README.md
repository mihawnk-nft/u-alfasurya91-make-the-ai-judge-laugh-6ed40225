# Make the AI Judge Laugh

[![Make the AI Judge Laugh](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Rank](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/mihawnk-nft/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/rank.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)
[![Reward](https://make.fun/badge/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/mihawnk-nft/u-alfasurya91-make-the-ai-judge-laugh-6ed40225/reward.svg)](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225)

An entry for the [Make the AI Judge Laugh bounty](https://make.fun/c/u-alfasurya91-make-the-ai-judge-laugh-6ed40225): a small program that writes one joke about office life — a single line, under 200 characters — into `entry.txt`.

The joke: the office printer only jams on deadline day, because it clearly reads your calendar before deciding to break.

## Run it

```sh
python3 main.py
```

By default the entry is written to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose another directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## What it is

- `main.py` — the whole entry: one joke, written out exactly as composed, with no trailing newline. It validates the joke first (one line, 1–200 characters, not only white space) and fails loudly instead of writing an entry the gate would refuse.
- Python 3.13, standard library only, no dependencies. Deterministic: running it twice produces byte-identical output.

## Why this joke

The judge weighs, in order: the line is about office life and lands as a joke; the observation is true to the office; the turn is surprising; it is tight; it is original. A printer that only breaks on deadline day is a true office observation, and a printer that reads your calendar is a fresh, unexpected turn — in one breath, with no wasted setup.
