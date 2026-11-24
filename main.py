#!/usr/bin/env python3
# One-Star Review of Something Essential: a deadpan one-star review of sleep.
#
# The program writes one single-line review, 100 characters, to
# /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# Pure standard library, no network, no clock, no randomness: every run
# writes the exact same bytes.
#
# The review: sleep takes eight hours a night, every night, with no
# rollover and no refunds, and still leaves you waking up in debt. The
# grievance is the small daily annoyance everyone recognises but has never
# seen filed as a complaint: you pay in full, every night, and still owe
# more in the morning. The sting lands in the last few words, after the
# complaint has been read straight, and the whole thing is one joke told
# cleanly in the deadpan language of a terms-of-service page.

import os

REVIEW = (
    "Sleep: eight hours a night, every night, no rollover, no refunds, "
    "and I still wake up owing it more."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    # Post-write gate: read the file back and confirm it holds exactly
    # the review, non-empty and inside the 1-160 character gate, so a
    # truncated or empty write can never pass silently.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != REVIEW:
        raise ValueError("written output does not match the review")
    if not written:
        raise ValueError("written output is empty")
    if not (1 <= len(written) <= 160):
        raise ValueError(f"written output is {len(written)} characters, must be 1-160")


if __name__ == "__main__":
    main()
