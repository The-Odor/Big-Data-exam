#!/usr/bin/python3
import sys
sys.path.append('../') #allows access functions in parallel folder
import ProjectFunctions.functions as proj

cleanBody, mapper_core, parser = proj.cleanBody, proj.mapper_core, proj.xmlparser

"""
xmlmapper(source, infile=sys.stdin)
main mapper function, uses cleanBody() and mapper_core()
Indexes all words in bodies of questions, titles and
answers according to the post Id of the posts it
appears in

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

    #Extracting the relevant section from the file
    for row in parsed:
        mappedWords = {}
        if (row.attrib["PostTypeId"] in ["1", "2"]):
            body = row.attrib["Body"]

            #Differentiates between answer(1) and question(2)
            if row.attrib["PostTypeId"] == "1":
                id    = row.attrib["Id"]
                title = row.attrib["Title"]
            elif row.attrib["PostTypeId"] == "2":
                id    = row.attrib["ParentId"]
                try:
                    title = row.attrib["Title"]
                except KeyError:
                    title = "" #answers have no title

            body = title + body
            body = cleanBody(body)

            id = [int(id)]*len(body)

            #Combiner
            for word in body:
                if word == "":
                    continue
                if word in mappedWords:
                  mappedWords[word].append()

            mapper_core([body, id], "double")

xmlmapper("Title")
