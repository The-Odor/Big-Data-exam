#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word,count = line.split()

    ids = []

    if current_word == word and current_count == count:
        pass
    elif current_word == word:
        if current_word:
            ids.append(count)
    else:
        ids.append(count)
        idprint = ""
        for id in ids:
            idprint += "," + id
        print("%s, %s"%(current_word, idprint))

        current_word = word

if current_word== word:
    ids.append(count)
    idprint = ""
    for id in ids:
        idprint += "," + id
    print("%s, %s"%(current_word, idprint))

    current_word = word
