# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:53:52 2019

@author: Live to Game_
"""

import xml.etree.ElementTree as ET
from re import sub
import string
from sys import stdin

nonAscii = string.punctuation

mytree = ET.parse("Posts.xml")
myroot = mytree.getroot()

for i in myroot.attrib:
    print(i)

if stdin.strip().startswith("<row"):

    for x in myroot[90:94]:
      body = x.attrib["Body"] #Finds body
      body = body.lower() #makes lowercase

      body = sub('<.+?>', '', body) #removes all cases of <something>

      for i in nonAscii:
        #removes all punctuation and numbers
        body = body.replace(i, "")

      wordlen = len(body.split(" ")) #amount of words

    #  print(body + "\n", wordlen, x.attrib["Id"])


      for word in body.strip().split(" "):
          print("%s\t%d" % (word, 1))


#%%

a = "            "
while "  " in a:
    a = a.replace("  ", " ")


nonascii = "12345687"
word = "a"



print(any((i in nonascii for i in word)))

if len(word) <= 2 and any(i in nonascii for i in word):
    print("lmao")
else:
    print("%s\t%d"%(word, 1))

#
#print(a, len(a))
#print(a.split(" "))
##print("        ".split(" "))
#
#print("hello".split("hello"))


#%%
dict{"security":[post1, post2]
     "bitcoin":[post65, posbullion]}