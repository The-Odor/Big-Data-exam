#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, parser = proj.cleanBody, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody()
Counts words in xml-files, where the bodies are defined as
questions (PostTypeId = 1). Uses a combiner

input:
  string source           : xml-tag to extract from
                            infile

  string infile=sys.stdin : parsed xml-file
                            if given a string, will look in
                            working directory for xml to parse

returns:
  None, prints words into format acceptable by Hadoop
"""
def xmlmapper(source, infile=sys.stdin):
    parsed = parser(infile)

    allwords = {}

    # Iterates through each xml-row and extracts data
    for post in parsed:
        if (post.attrib["PostTypeId"] == "1"):
            body = post.attrib[source]

            words = cleanBody(body)

            #Combiner
            for word in words:
                if word == "":
                    continue
                if word in allwords:
                    allwords[word]+= 1
                else:
                    allwords[word] = 1

    #Converts allwords from dict to list
    wordslist = []
    for word in allwords:
        wordslist.append([word, allwords[word]])

    wordslist.sort(key=lambda x: x[-1])

    for word, count in wordslist:
        print("%s %d "%(word, count))

xmlmapper("Body")
