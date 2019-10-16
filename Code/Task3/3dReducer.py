#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Counts the amount of times the word useless is used

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reducer():
    useless_count = 0

    for line in sys.stdin:
        useless_count += int(line.strip())

    print("The word useless occurs %d times" %(useless_count))

reducer()
