#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
creates a dictionary over unique tags in an xml-file

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reducer():
    current_word = None
    word = None

    for line in sys.stdin:
        line = line.strip()
        word = line.split()[0]

        if current_word ==word:
            pass
        else:
            if current_word:
                print("%s "%(current_word))
            current_word = word
 
    if current_word== word:
        print("%s "% (current_word))

reducer()