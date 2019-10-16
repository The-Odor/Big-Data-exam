#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody() and mapper_core()
Counts words in xml-files, where the bodies are defined as
questions (PostTypeId = 1). Removes stopwords as defined in
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

def xmlmapper(source, infile=sys.stdin):
    parsed = parser(infile)

    # Iterates through each xml-row and extracts data
    for x in parsed:
        if (x.attrib["PostTypeId"] == "1"):
            body = x.attrib[source]

            words = cleanBody(body)

            for Stop in StopW:
                while Stop in words:
                    words.remove(Stop)

            mapper_core(words)


with open("StopWords.txt","r") as StopWords:
    StopW = StopWords.readlines()
    StopW = [i[:-1] for i in StopW[:-1]] + [StopW[-1]]
    for i in range(len(StopW)):
        StopW[i] = StopW[i].replace("'","")

xmlmapper("Title")
