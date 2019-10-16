#!/usr/bin/python3
import sys
# using a dictionary to map words to their counts

"""
reducer()
main reducer function
Counts words in xml-files, where the bodies are defined as
questions (PostTypeId = 1). Stopwords removed as defined in
stopwords.txt, taken taken on 16.10.2019 from
https://raw.githubusercontent.com/naimdjon/stopwords/master/stopwords.txt

input:
  string source           : xml-tag to extract from
                            infile

  string infile=sys.stdin : parsed xml-file
                            if given a string, will look in
                            working directory for xml to parse

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
