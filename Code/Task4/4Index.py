#!/usr/bin/python3
import sys
import xml.etree.ElementTree as ET
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core  = proj.cleanBody, proj.mapper_core

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody() and mapper_core()
Lists unique words in xml-files, where the bodies are 
defined as questions (PostTypeId = 1)

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
    if not isinstance(infile, str):
        infile = infile.detach()

    #Making the xml-file readable
    mytree = ET.parse(infile)
    myroot = mytree.getroot()

    #Extracting the relevant section from the file
    for x in myroot:
        if (x.attrib["PostTypeId"] == "1"):
            #Fetching the content of body
            title = x.attrib["Title"]
            body = x.attrib["Body"]
            id   = x.attrib["Id"]

            body = title + body

            body = cleanBody(body)

            id = id*len(body)

            # print(type(id), type(body))

            mapper_core([body, id], "double")

xmlmapper("Title")

