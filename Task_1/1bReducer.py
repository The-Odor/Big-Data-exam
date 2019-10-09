#!/usr/bin/python3

import sys

current_word = None

for line in sys.stdin:
    word, count = line.strip().split()
    if current_word:
        if word == current_word:
            continue
        print("%s\t%d" % (current_word, 1))

    current_word = word

print("%s\t%d" % (current_word, 1))