#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core  = proj.cleanBody, proj.mapper_core

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

    for x in myroot:

        #Fetching the content of body
        body = x.attrib[source]
        rep = x.attrib["Reputation"]
        #words = cleanBody(body)
        #print([body, rep])

        mapper_core([[body], [rep]], "double")

xmlmapper("Id")
