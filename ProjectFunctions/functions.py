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
mapper_core(words)
maps list of words into format acceptable by Hadoop
ignores groups of characters containing fewer than 2 characters
or containing characters listed in string.digits or string.punctuation

input:
  string words : words wanted to be passed into Hadoop

returns:
  None, prints words into format acceptable by Hadoop
"""
def mapper_core(words):
    for word in words:
        if (len(word) < 2 and (i in ignore_char for i in word)):
            #TODO: check whether second check is redundant due
            #substitution in cleanBody in ignore_char-loop
            pass
        else:
            print("%s  %s" %(word,1)) #Emit the word

