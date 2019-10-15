#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    templist= line.split(" ");
    id, score = templist[:2]
    tempText = templist[2:]
    Title=" ".join(tempText)

    #id, score = templst[:2]
    #Title = templst[2:]

    #Title = temptext


    score = int(score)
    if current_word ==id:
        current_count += score
    else:
        if current_word:
            print("%s,%s,%s"%(current_word, Title, current_count))
        current_word = id
        current_count = score
if current_word== id:
    print("%s,%s,%s "% (current_word, Title, current_count ))
