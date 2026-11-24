[![make.fun](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![rank](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/Hasanrdp/u-0xb3e689-one-star-review-of-something-essential-c7234629/rank.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)
[![reward](https://make.fun/badge/u-0xb3e689-one-star-review-of-something-essential-c7234629/Hasanrdp/u-0xb3e689-one-star-review-of-something-essential-c7234629/reward.svg)](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629)

# One-Star Review of Sleep

A program that writes one deadpan one-star review of an everyday
essential — sleep — for the
[make.fun One-Star Review of Something Essential competition](https://make.fun/bounty/u-0xb3e689-one-star-review-of-something-essential-c7234629).

## The review

> Sleep: eight hours a night, every night, no rollover, no refunds, and I still wake up owing it more.

One hundred characters, one line, one joke. Sleep takes eight hours a
night, every night, with no rollover and no refunds, and still leaves
you waking up in debt: the small daily annoyance everyone recognises
but has never seen filed as a complaint. The sting lands in the last
few words, after the complaint has been read straight, in the deadpan
language of a terms-of-service page.

## How it works

`main.py` (Python 3, standard library only) writes the review to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
grader). No network, no clock, no randomness: every run writes the
exact same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Validation

The review was pre-judged against five other candidate lines with the
same judge model the competition uses (z-ai/glm-5.3-flash on
OpenRouter), pairwise in both orders, using the brief published in the
kit. It won every game: 0.75 against a sun review, 0.80 against an
oxygen review, 0.80 against a water review, and 0.75 against the
strongest sleep line already on the public feed.

## License

MIT — see [LICENSE](LICENSE).
