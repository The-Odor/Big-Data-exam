#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(infile)
main mapper function, uses cleanBody() and mapper_core()
Lists top 10 users in terms of their reputation

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
    for miner in parsed:
        name = miner.attrib[source]
        rep = int(miner.attrib["Reputation"])
        words = " ".join(cleanBody(name))

        name = cleanBody(name)

        mapper_core([name, [rep]], "double")

xmlmapper("DisplayName")
