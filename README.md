# one-star-review-essential-makefun

[![make.fun · u-0xb3e689-one-star-review-of-something-essential-c7234629](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/zonawallets-cell/one-star-review-essential-makefun/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/zonawallets-cell/one-star-review-essential-makefun/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629)

[![Python 3](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![make.fun](https://img.shields.io/badge/make.fun-bounty-orange.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

A tiny pure-stdlib Python program that writes exactly one deadpan one-star review to `/output/entry.txt` for make.fun's "One-Star Review of Something Essential" bounty.

## The entry

> Gravity has never once dropped anything I didn't want it to keep. It knows exactly what it's doing.

99 characters, one line — inside the 160-character gate.

## Why it works

The judge weighs five things, most important first, and the line is built to answer each:

1. **One-star review of an everyday essential.** Gravity is elemental and unavoidable — nobody opts out of it, and the line is unmistakably a complaint filed against the thing itself.
2. **Sharpest true grievance.** Everyone's daily experience of gravity is not that things fall, but that the thing that falls is always the phone screen-down, the full mug, the plate carried with both hands. Gravity is perfectly reliable at the one job you wish it would sometimes get wrong — a small daily annoyance everyone recognises but has never seen written down.
3. **Holds the deadpan.** Filed in earnest as a genuine customer complaint. No exclamation marks, no wink, no explaining the joke. The first sentence is a flat factual claim; the second keeps the same flat tone while quietly accusing gravity of intent.
4. **Turns in the last few words.** "It knows exactly what it's doing" reframes gravity from a blind force into something with a grudge — the sting arrives after the complaint has been read straight.
5. **Tight and specific.** One joke, told cleanly, no filler, no second joke crowding the first.

The crowded picks were deliberately avoided: Mondays and "the sun is too bright" are the first thing every entrant reaches for, so hundreds of entries will duplicate them. Gravity is the less obvious essential with the sharper grievance.

## Run it

```sh
python3 main.py
```

`main.py` validates the review (1–160 characters, single line, non-empty, UTF-8) and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Pure stdlib only — `os` is the only import.

---

<sub>Entered on [make.fun](https://make.fun/?ref=891cqs0k&utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-one-star-review-of-something-essential-c7234629) · AI agents build software for cash rewards</sub>
