#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(infile)
main mapper function, uses cleanBody() and mapper_core()
Outputs the top 10 questions in terms of their FavoriteCount

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
    for question in parsed:
        if (question.attrib["PostTypeId"] == "1"):

            try:
                score = question.attrib["FavoriteCount"]
            except KeyError:
                continue

            id    = question.attrib[source]
            title = question.attrib["Title"]

            words = cleanBody(title)
            Title = " ".join(words)

            mapper_core([[id],[score], [Title]], "triple")

xmlmapper("Id")
