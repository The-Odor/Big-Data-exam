#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    id,rep = line.split(" ");

    rep = int(rep)
    if current_word ==id:
        current_count += rep
    else:
        if current_word:
            print("%s %s "%(current_word, current_count))
        current_word = id
        current_count = rep
if current_word== id:
    print("%s %s "% (current_word, current_count))
