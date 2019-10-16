#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Outputs top 10 popular usernames

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reduce():
    current_word = None
    current_count = 0
    wholelist = []


    for line in sys.stdin:
        line = line.strip()
        Name, count= line.split("|")
        count = int(count)
        if current_word == Name:
            current_count += count
        else:
            if current_word:
                wholelist.append([current_word,current_count])
            current_word = Name
            current_count = count
    if current_word == Name:
        wholelist.append([current_word,current_count])
        
    wholelist.sort(key = lambda x: -x[1])

    for i in range(10):
        print(wholelist[i][0], wholelist[i][1])

reduce()