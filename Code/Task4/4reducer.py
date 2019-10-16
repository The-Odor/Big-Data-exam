#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_id = 0
word = None
ids = []


for line in sys.stdin:
    line = line.strip()

    try:
        word,id = line.split()
        id = int(id)
    except ValueError:
        continue

    if current_word == word and current_id == id:
        pass
    elif current_word == word and current_id != id:
        if current_word and not id in ids:
            ids.append(id)
    else:
        ids.append(id)
        idprint = ""
        for id in ids:
            idprint += "," + str(id)
        print("%s, %s"%(current_word, idprint))

        current_word = word
        ids = []

if current_word== word:
    ids.append(id)
    idprint = ""
    for id in ids:
        idprint += "," + str(id)
    print("%s, %s"%(current_word, idprint[1:]))

    current_word = word
