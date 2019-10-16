#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(infile)
main mapper function, uses cleanBody() and mapper_core()
Combined with 1ePig.pig, lists top 10 words (not counting
stopwords) found in titles

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
    for titles in parsed:
        if (titles.attrib["PostTypeId"] == "1"):
            title = titles.attrib[source]

            words = cleanBody(title)

            for Stop in StopW:
                if Stop in words:
                    words.remove(Stop)

            mapper_core(words)


# Extracts stopwords to a useable format
with open("StopWords.txt","r") as StopWords:
    StopW = StopWords.readlines()
    StopW = [i[:-1] for i in StopW[:-1]] + [StopW[-1]]
    for i in range(len(StopW)):
        StopW[i] = StopW[i].replace("'","")

xmlmapper("Title")
