#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody() and mapper_core()
Outputs the number of questions that have at least 1 answer

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
    for post in parsed:
        if (post.attrib["PostTypeId"] == "1" and\
                int(post.attrib["AnswerCount"]) > 0):

            count += 1

    print("Answers %d"%(count))

xmlmapper("AnswerCount")
