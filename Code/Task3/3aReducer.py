#!/usr/bin/python3
import sys

"""
xmlmapper(source, infile=sys.stdin)
main reducer function
Counts bigrams in xml-files, where the bodies are defined as 
questions (PostTypeId = 1)

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reducer():
    current_word = None
    current_count = 0
    word = None
    
    most_common = ["NOTABIGRAM", 0]

    for line in sys.stdin:
        line = line.strip()
        word,count = line.split("|")

        count = int(count)
        if current_word ==word:
            current_count += count
        else:
            if current_word:
                if current_count > most_common[1]:
                    most_common = [current_word, current_count]
            current_word = word
            current_count = count
    if current_word== word:
        if current_count > most_common[1]:
            most_common = [current_word, current_count]
        
    print(most_common[0],",", most_common[1])

reducer()