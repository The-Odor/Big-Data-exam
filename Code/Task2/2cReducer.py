#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    id,rep = line.split();

    count = int(count)
    if current_word ==word:
        current_count += count
    else:
        if current_word:
            print("%s %s "%(current_word, current_count))
        current_word = word
        current_count = count
if current_word== word:
    print("%s %s "% (current_word, current_count))
