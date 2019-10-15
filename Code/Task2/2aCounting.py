#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

#TODO: update documentation
"""
xmlmapper(infile)
main mapper function, uses cleanBody() and mapper_core()

input:
  string infile=sys.stdin : parsed xml-file
                            if given a string, will look in
                            working directory for xml to parse

returns:
  None, prints words into format acceptable by Hadoop
"""
def xmlmapper(source, infile=sys.stdin):
    if not isinstance(infile, str):
        infile = infile.detach()
    mytree = ET.parse(infile)
    myroot = mytree.getroot()
    UserID = []
    for x in myroot:

            #Fetching the content of body
            UserID.append(x.attrib[source])

    print("Total Unique Users: " + str(len(UserID)))
xmlmapper("Id")
