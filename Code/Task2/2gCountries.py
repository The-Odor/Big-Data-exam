#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody()
Counts amount of users in a given location

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
    for post in parsed:
        try:
            Location = post.attrib[source]
        except KeyError:
            continue

        Location = Location.split(",")[-1]
            
        loc = " ".join(cleanBody(Location))

        print(loc, "|", 1)

xmlmapper("Location")
