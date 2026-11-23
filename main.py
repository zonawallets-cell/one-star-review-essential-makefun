"""One-Star Review of Something Essential — writes one review to /output/entry.txt.

Pure stdlib (os only). The review is a single deadpan line about gravity:

    Gravity has never once dropped anything I didn't want it to keep.
    It knows exactly what it's doing.

Why gravity: the brief lists the sun, gravity, sleep, water, oxygen and
Mondays as the everyday essentials. Mondays and "the sun is too bright"
are the crowded picks — the first thing every entrant reaches for, so
hundreds of entries will duplicate them. Gravity is elemental, universal
and unavoidable, and it has a grievance nobody else states quite this
way: it never fails at random, it fails precisely where it hurts.

Why this grievance is the sharpest true one: everyone's daily experience
of gravity is not that things fall — it is that the thing that falls is
always the phone screen-down, the full mug, the plate you were carrying
with both hands. Gravity is perfectly reliable at the one job you wish
it would sometimes get wrong. That is a real, small, daily annoyance
everyone recognises but has never seen written down as a complaint.

How the deadpan holds: the whole line is filed in earnest, as a genuine
customer complaint. No exclamation marks, no wink, no "lol", no
explaining the joke. The first sentence is a flat factual claim a
reviewer could believe; the second sentence keeps the same flat tone
while quietly accusing gravity of intent.

Where it turns: the sting lands in the last few words — "It knows
exactly what it's doing." Up to that point the review reads straight;
the turn reframes gravity from a blind force into something with a
grudge, and that is the joke. One joke, told cleanly, no second joke
crowding the first, no filler.

Char count: 99 characters, well under the 160-character gate, single
line, no trailing newline in the entry file.
"""

import os

MAX_CHARS = 160

# The one-star review, exactly as submitted.
REVIEW = (
    "Gravity has never once dropped anything I didn't want it to keep. "
    "It knows exactly what it's doing."
)


def validate(review):
    """Enforce the gate: 1-160 chars, single line, non-whitespace, UTF-8."""
    if not isinstance(review, str):
        raise ValueError("review must be a string")
    review.encode("utf-8")
    if not review.strip():
        raise ValueError("review must not be only whitespace")
    if len(review) > MAX_CHARS:
        raise ValueError(
            "review must be at most %d characters, got %d"
            % (MAX_CHARS, len(review))
        )
    if "\n" in review or "\r" in review:
        raise ValueError("review must be a single line")
    return True


def main():
    validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
