#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody()
Counts trigrams (list of tree words) in xml-files, 
where the bodies are defined as questions (PostTypeId = 1)

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
        if (post.attrib["PostTypeId"] == "1"):
            body = post.attrib[source]

            words = cleanBody(body)

            for i in range(len(words)-2):
                print("{} {} {} | 1"\
                .format(words[i], words[i+1], words[i+2]))

xmlmapper("Title")
