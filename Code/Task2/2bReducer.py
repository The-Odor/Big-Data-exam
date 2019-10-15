#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    #word,count = line.split();


    if current_word ==line:
        pass
    else:
        if current_word:
            print("%s "%(current_word))
        current_word = line

if current_word== line:
    print("%s "% (current_word))
