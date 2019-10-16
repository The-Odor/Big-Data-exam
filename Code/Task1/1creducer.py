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
    total_average = 0

    for line in sys.stdin:
        total_average += int(line.strip())
    
    print(total_average)

reducer()