#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Outputs top 10 questions in terms of their Score

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reducer():
    current_word = None
    current_count = 0
    wholelist = []

    for line in sys.stdin:
        line = line.strip()
        templist  = line.split(" ")
        Id, score = templist[:2]
        tempText  = templist[2:]
        Title = " ".join(tempText)

        score = int(score)
        if current_word ==Id:
            current_count += score
        else:
            if current_word:
                wholelist.append([current_word, Title, current_count])
            current_word = Id
            current_count = score
    if current_word== Id:
        print("%s,%s,%s "% (current_word, Title, current_count))

    wholelist.sort(key = lambda x: -x[2])
    for i in range(10):
        out = ""
        for j in wholelist[i]:
            out += str(j) + ","
        # for i in out:
        #     print(i, end=", ")
        # print()

        # print(wholelist[i],"\n")
        print(out[:-1])

reducer()