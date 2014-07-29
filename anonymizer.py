#!/usr/bin/env python
#coding=utf-8
from mondrian import mondrian
from utils.read_data import read_data
from utils.save_result import save_to_file
import sys
import pdb
# Poulis set k=25, m=2 as default!

if __name__ == '__main__':
    K = 10
    try:
        K = int(sys.argv[1])
    except:
        pass
    #read record
    data = read_data()
    # remove duplicate items
    print "Begin Partition"
    result = mondrian(data, K)
    save_to_file(result)
    print "Finish Partition!!"
    # print "Begin Evaluation"
    # are = average_relative_error(att_tree, trans, result)
    # print "Average Relative Error: %.2f" % are
