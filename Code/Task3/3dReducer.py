#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Outputs an integer of how many questions (PostTypeId = 1)
have 10 or more words in their titles (including stopwords)

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
