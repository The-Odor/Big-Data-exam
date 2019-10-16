#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

parser = proj.xmlparser

"""
xmlmapper(infile)
main mapper function, uses cleanBody() and mapper_core()
Counts how many unique users there is in an xml database

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
    UserID = []
    for Id in parsed:

            UserID.append(Id.attrib[source])

    print(len(UserID))
xmlmapper("Id")
