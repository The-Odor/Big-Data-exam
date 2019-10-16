#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody()
Outputs the average amount of answers per question

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

    total = 0
    count = 0
    # Iterates through each xml-row and extracts data
    for post in parsed:
        if (post.attrib["PostTypeId"] == "1"):
            total += int(post.attrib[source])
            count += 1

    average = total/count
    print(average)

xmlmapper("AnswerCount")