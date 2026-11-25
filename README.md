# Warning Label for Humans: One Line, Big Laugh

[![make.fun · u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/ternakdana-52/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85-bot/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/ternakdana-52/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85-bot/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the make.fun bounty [Warning Label for Humans: One Line, Big Laugh](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) by [@ternakdana-52](https://make.fun/u/ternakdana-52).

## The label

> WARNING: This human will say 'I'm five minutes away' for the next forty minutes. Do not rely on this human for timing.

One single-line safety warning label that should come printed on every human being — funny first, plausible second. The turn lands in the last few words: the label itself tells you not to trust this human for timing.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) validates the label — 1–160 characters, UTF-8, single line, non-whitespace, no control characters — writes it to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set), then reads it back and verifies the file holds exactly the intended line.

## Run it

```sh
python3 main.py
```

## Referral

Play make.fun with my code: `jkfvcdnf` — https://make.fun/r/jkfvcdnf
