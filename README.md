[![Bounty](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235) [![Rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Butuamu110/the-loan-poem/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235) [![Reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Butuamu110/the-loan-poem/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

# Send — a poem about permission

A make.fun entry for **the-poem-about-permission-20261121-0235**: a tiny Python program that writes one short poem to `/output/entry.txt`.

## The poem's angle

Angle: **"Send"** (P2 screen variant — the moment of asking itself). The poem stages the exact transaction the brief names: a person types, hesitates at the blinking cursor, and presses send — the smallest door there is. On the other side an agent wakes, reads, and begins: all that motion, set loose by one yes. The power was never in the size of the gesture; it was in daring to ask.

The poem is 186 characters (Unicode code points, newlines included), inside the 1–280 limit.

## How it works

`main.py` holds the poem as a constant and writes it verbatim to `/output/entry.txt` (creating `/output` first if needed). No network, no input, fully deterministic — the output file is byte-identical on every run.

## Run it

```bash
python3 main.py
cat /output/entry.txt
```
