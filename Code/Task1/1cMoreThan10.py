#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(infile)
main mapper function, uses cleanBody()
Outputs an integer of how many questions (PostTypeId = 1)
have 10 or more words in their titles (including stopwords)

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

    count = 0

    # Iterates through each xml-row and extracts data
    for titles in parsed:
        if titles.attrib["PostTypeId"] == "1":
            title = titles.attrib[source]

            words = cleanBody(title)

            if len(words) >10 :
                count += 1
    
    print (count)

xmlmapper("Title")
