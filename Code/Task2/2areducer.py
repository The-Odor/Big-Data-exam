#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Counts how many unique users there is in an xml database

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