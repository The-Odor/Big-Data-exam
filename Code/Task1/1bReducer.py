#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Lists unique words in xml-files, where the bodies are 
defined as questions (PostTypeId = 1)

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
        word,count = line.split()

        if current_word ==word:
            pass
        else:
            if current_word:
                print("%s "%(current_word))
            current_word = word

    if current_word== word:
        print("%s "% (current_word))

reducer()
