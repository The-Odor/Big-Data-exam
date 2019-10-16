#!/usr/bin/python3
import sys

"""
reducer()
main reducer function
Lists all unique users in an xml databse by unique Id
and displayname

input:
  None

returns:
  None, prints words into format acceptable by Hadoop
"""
def reduce():
    current_name = None
    current_rep = 0
    name = None

    for line in sys.stdin:
        line = line.strip()
        rep,name = line.split("|")


        if current_rep == rep:
            pass
        else:
            if current_rep:
                print("%s %s"%(current_rep, current_name))
            current_rep = rep
            current_name = name

    if current_rep== rep:
        print("%s %s"% (current_rep, current_name))

reduce()