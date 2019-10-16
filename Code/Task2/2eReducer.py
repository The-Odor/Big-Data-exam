#!/usr/bin/python3
import sys

def reduce():
    current_word = None
    current_count = 0
    wholelist = []

    for line in sys.stdin:
        line = line.strip()
        templist = line.split(" ")
        id, score = templist[:2]
        tempText = templist[2:]
        Title = " ".join(tempText)

        score = int(score)
        if current_word ==id:
            current_count += score
        else:
            if current_word:
                wholelist.append([current_word, Title, current_count])
            current_word = id
            current_count = score
    if current_word== id:
        wholelist.append([current_word, Title, current_count])

    wholelist.sort(key = lambda x: -x[2])
    for i in range(10):
        out = wholelist[i]

        idout    = out[0]
        questout = out[1]
        scoreout = out[2]

        #Text formatting
        outTrue = idout + ", " + " "*(6-len(idout)) +\
                    questout + ", " + str(scoreout)

        print(outTrue)

reduce()