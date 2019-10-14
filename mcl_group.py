#!/usr/bin/python
#File created on 2019/7/18

__author__ = "Wang,Yansu"
__copyright__ = "Copyright 2019, JSNU"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Wang,yansu"
__email__ = "Wangys_c@hotmail.com"

import sys
import re
from optparse import OptionParser
import numpy as np
import string

def MakeOption():
    # make option
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=] -f [ref=] -o[--output=]",
                          version="%prog 1.0")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="group.txt",
                      default=False)
    parser.add_option("-f", "--ref", action="store", dest="id",
                      help="sample_id.txt",
                      default=False)
    parser.add_option("-o", "--output", action="store", dest="output",
                      help="orthomcl_table.txt",
                      default=False)
    (options, args) = parser.parse_args()
    # extract option from command line
    input = options.input
    id = options.id
    output = options.output
    return (input,id, output)

def main():
    input,id,output = MakeOption()
    output = open(output,"w")
    input_file = open(input,"r")
    id = open(id,"r")
    id_dict = {}
    a = []
    output.write("\t"+"sample"+ "\t")
    for i in id:
        i = i.replace("\n", "")
        id_dict[i] = 0
        output.write(("%s\t" % (i)))
    for j in input_file:
        group = "".join(j.split(":")[0])
        a.append("\n")
        a.append(group)
        for key in id_dict:
            key2 = str(key+"_")
            if key2 in str(j):
                id_dict[key]+=j.count(key2)
            else:
                id_dict[key] = 0
            a.append(id_dict[key])
    b = "\t".join('%s' %id for id in a)
    output.write("%s\n"%(b))
    output.close()
if __name__ == '__main__':
    main()
