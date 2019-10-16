#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Lists all unique users in an xml databse

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reduce():
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

reduce()