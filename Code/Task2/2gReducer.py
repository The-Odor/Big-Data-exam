#!/usr/bin/python3
import sys

"""
xmlmapper(source, infile=sys.stdin)
main reducer function
Counts amount of users in a given location

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reducer():
    current_word = None
    current_count = 0
    word = None

    for line in sys.stdin:
        line = line.strip()
        word,count = line.split("|")

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

reducer()