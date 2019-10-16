import xml.etree.ElementTree as ET
import string
import sys
from re import sub

#Defines characters to be ignored, 123?{/¤ etc.
ignore_char = string.digits + string.punctuation



"""
cleanBody(body)
Formats string for mapper function
non-case sensitive, removes HTML formatting, treats anything separeted
by blank space or / as separate words. Mispellings, names, filenames,
functionnames etc. will be counted as separate words

input:
  string body : string to be formatted

returns:
  string body : formatted string
"""
def cleanBody(body):
    body = body.lower()
    body = ascii(body)
    body = sub("<.+?>","",body)
    body = body.replace("/", " ")
    body = body.strip()

    for i in ignore_char:
        body = body.replace(i, "")

    body = body.split(" ")

    return body


"""
mapper_core(words, mode="single")
maps list of words into format acceptable by Hadoop
ignores groups of characters containing fewer than 2 characters
or containing characters listed in string.digits or string.punctuation

input:
  list words : words wanted to be passed into Hadoop
               if 

returns:
  None, prints words into format acceptable by Hadoop
"""
def mapper_core(words, mode="single"):
    if mode == "single":
        for word in words:
            if word not in ["", " "]:
              print("%s %s" %(word,1)) #Emit the word

    elif mode == "double":
        in1, in2 = words
        for word, count in zip(in1,in2):
            if word not in ["", " "]:
                print("%s %s" %(word,count)) #emit the words

    elif mode == "triple":
        in1, in2,in3  = words
        for id, score, title in zip(in1,in2,in3):
            print("%s %s %s" %(id,score, title)) #emit the words


"""
xmlparser(infile):
Our chosen method for interpreting our dataset. Takes up
a larger amount of memory for larger filesizes, but is
fast enough and small enough for its application here

input:  
  infile : unparsed xml-file

returns:
  myroot : parsed xml-file
"""
def xmlparser(infile):
    if not isinstance(infile, str):
        infile = infile.detach()
    mytree = ET.parse(infile)
    myroot = mytree.getroot()
    return myroot