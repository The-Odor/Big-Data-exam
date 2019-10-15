#!/usr/bin/python3
import sys
from operator import itemgetter
# using a dictionary to map words to their counts
current_word = None
current_count = 0
word = None
wholelist = []

for line in sys.stdin:
    line = line.strip()
    Name, count= line.split("|");
    #print(line)
    count = int(count)
    if current_word ==Name:
        current_count += count
    else:
        if current_word:
            #print("%s %s"%(current_word, current_count))
            wholelist.append([current_word,current_count])
        current_word = Name
        current_count = count
if current_word == Name:
    print("%s %s "% (current_word, current_count ))
    
wholelist.sort(key = lambda x: -x[1])
for i in range(10):
    print(wholelist[i],"\n")
