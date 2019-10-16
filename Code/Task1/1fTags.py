#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
creates a dictionary over unique tags in an xml-file

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

    tag = None
    # Iterates through each xml-row and extracts data
    for tags in parsed:
        try:
            tag = tags.attrib[source]  
        except KeyError:
            continue

        tag = tag.replace(">", " ")
        tag = tag.replace("<", "")
        words = cleanBody(tag)

        mapper_core(words)

xmlmapper("Tags")
