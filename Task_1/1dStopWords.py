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
        if (x.attrib["PostTypeId"] == "1"):
            #Fetching the content of body
            body = x.attrib[source]

            words = cleanBody(body)


            for Stop in StopW:
                if Stop in words:
                    words.remove(Stop)
            print(words)
            #mapper_core(words)


with open("StopWords.txt","r") as StopWords:
    StopW = StopWords.readlines()
    StopW = [i[:-1] for i in StopW[:-1]] + [StopW[-1]]
    for i in range(len(StopW)):
        StopW[i] = StopW[i].replace("'","")
        #print(StopW[i])

xmlmapper("Title")
