#!/usr/bin/env python
#coding=utf-8

# Read data and read tree fuctions for INFORMS data
# user att ['DUID','PID','DUPERSID','DOBMM','DOBYY','SEX','RACEX','RACEAX','RACEBX','RACEWX','RACETHNX','HISPANX','HISPCAT','EDUCYEAR','Year','marry','income','poverty']
# condition att ['DUID','DUPERSID','ICD9CODX','year']

from models.gentree import GenTree

__DEBUG = False


def read_tree(flag=0):
    """read tree from data/tree_*.txt, store them in att_tree
    """
    print "Reading Tree"
    if flag == 1:
        return read_tree_file('ICD9CODX')
    elif flag == 2:
        return read_tree_file('even')
    else:
        return read_tree_file('BMS')

  
def read_tree_file(treename):
    """read tree data from treename
    """
    leaf_to_path = {}
    att_tree = {}
    prefix = 'data/treefile_'
    postfix = ".txt"
    treefile = open(prefix + treename + postfix,'rU')
    att_tree['*'] = GenTree('*')
    if __DEBUG:
        print "Reading Tree" + treename
    for line in treefile:
        #delete \n
        if len(line) <= 1:
            break
        line = line.strip()
        temp = line.split(';')
        # copy temp
        temp.reverse()
        for i, t in enumerate(temp):
            isleaf = False
            if i == len(temp)-1: 
                isleaf = True
            if not t in att_tree:
                # always satisfy
                att_tree[t] = GenTree(t, att_tree[temp[i - 1]], isleaf)
    if __DEBUG:
        print "Nodes No. = %d" % att_tree['*'].support
    treefile.close()
    return att_tree    


def read_data(flag=0):
    """read microda for *.txt and return read data
    """
    if flag:
        conditionfile = open('data/conditions05.csv', 'rU')
        print "Reading Data..."
        conditiondata = {}
        for i, line in enumerate(conditionfile):
            if i == 0:
                continue
            line = line.strip()
            # ignore first line of csv
            row = line.split(',')
            row[1] = row[1][1:-1]
            row[2] = row[2][1:-1]
            if row[1] in conditiondata.keys():
                conditiondata[row[1]].append(row[2])
            else:
                conditiondata[row[1]] = [row[2]]
        conditionfile.close()
        return conditiondata.values()
    else:
        bms_webview2 = open('data/BMS-WebView-2.dat', 'rU')
        print "Reading Data..."
        bmwdata = {}
        for line in bms_webview2:
            line = line.strip()
            row = line.split('\t')
            # use try and except to speed up comparision
            try:
                bmwdata[row[0]].append(row[1])
            except:
                bmwdata[row[0]] = [row[1]]
        bms_webview2.close()
        return bmwdata.values()
        if __DEBUG:
            print "Read Complete..."




