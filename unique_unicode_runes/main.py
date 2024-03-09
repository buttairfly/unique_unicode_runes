#!/usr/bin/env python3

import fileinput
from collections import defaultdict


def make_rune_dict(only_non_ascii: bool) -> defaultdict[str, int]:
    runes = defaultdict(int)
    for line in fileinput.input():
        for rune in line:
            if only_non_ascii:
                if ord(rune) > 0x7F:
                    runes[rune] += 1
            else:
                runes[rune] += 1
    return runes


def main():
    runes = make_rune_dict(True)
    for rune in sorted(runes):
        print(rune, end="")
    print()


if __name__ == "__main__":
    main()
