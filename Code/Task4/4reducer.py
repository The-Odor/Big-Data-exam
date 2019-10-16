#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Indexes all words in bodies of questions, titles and
answers according to the post Id of the posts it 
appears in

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reducer():
    current_word = None
    current_id = 0
    word = None
    ids = []

    for line in sys.stdin:
        line = line.strip()

        try:
            word,id = line.split()
            id = int(id)
        except ValueError:
            continue

        #Only updates current_word if different from word
        #Only appends id to index if different from current_id
        if current_word == word and current_id == id:
            pass
        elif current_word == word and current_id != id:
            if current_word and not id in ids:
                ids.append(id)
        else:
            ids.append(id)
            idprint = ""
            for id in ids:
                idprint += "," + str(id)
            print("%s, %s"%(current_word, idprint))

            current_word = word
            ids = []

    if current_word== word:
        ids.append(id)
        idprint = ""
        for id in ids:
            idprint += "," + str(id)
        print("%s, %s"%(current_word, idprint[1:]))

        current_word = word

reducer()
