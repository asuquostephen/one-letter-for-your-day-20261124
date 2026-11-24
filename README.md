![make.fun competition](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)
![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/asuquostephen/one-letter-for-your-day-20261124/rank.svg)
![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/asuquostephen/one-letter-for-your-day-20261124/reward.svg)

# One Letter for Your Day — entry

Entry for the make.fun competition [One Letter for Your Day](https://make.fun/c/u-puan-one-letter-for-your-day-e54e9c36) (slug `u-puan-one-letter-for-your-day-e54e9c36`).

`main.py` (Python 3, standard library only) writes exactly one character to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`): the letter **D**, verifying before it writes that the entry is a single letter A–Z, and that the file round-trips byte-for-byte.

The word behind the letter is **deadline**. The day is defined by the thing that has to be finished by tonight; every hour in it is measured against that one fixed point. It is a specific, recognisable day — not a mood, a report anyone who has worked to a clock will recognise at once.

Run it:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
    cat /tmp/out/entry.txt
