#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, parser = proj.cleanBody, proj.xmlparser

"""
xmlmapper(infile)
main mapper function, uses cleanBody() and mapper_core()
Lists all unique users in an xml databse by unique Id
and displayname

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
    for user in parsed:

        userID   = user.attrib[source]
        userName = user.attrib["DisplayName"]

        userName = " ".join(cleanBody(userName))

        print(userID + "|" + userName)
xmlmapper("Id")
