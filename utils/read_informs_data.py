"""
read informs dataset
"""

# !/usr/bin/env python
# coding=utf-8

# Read data and read tree fuctions for INFORMS data
# user att ['DUID','PID','DUPERSID','DOBMM','DOBYY','SEX','RACEX','RACEAX','RACEBX','RACEWX','RACETHNX','HISPANX','HISPCAT','EDUCYEAR','Year','marry','income','poverty']
# condition att ['DUID','DUPERSID','ICD9CODX','year']


__DEBUG = False
USER_ATT = ['DUID', 'PID', 'DUPERSID', 'DOBMM', 'DOBYY', 'SEX', 'RACEX', 'RACEAX',
            'RACEBX', 'RACEWX', 'RACETHNX', 'HISPANX', 'HISPCAT', 'EDUCYEAR',
            'Year', 'marry', 'income', 'poverty']
CONDITION_ATT = ['DUID', 'DUPERSID', 'ICD9CODX', 'year']
# Only 5 relational attributes and 1 transaction attribute are selected (according to Poulis's paper)
QI_INDEX = [3, 4, 6, 13, 16]
__DEBUG = False


def read_data():
    """
    read microda for *.txt and return read data
    """
    data = []
    userfile = open('data/demographics.csv', 'rU')
    conditionfile = open('data/conditions.csv', 'rU')
    userdata = {}
    # We selet 3,4,5,6,13,15,15 att from demographics05, and 2 from condition05
    # print "Reading Data..."
    for i, line in enumerate(userfile):
        line = line.strip()
        # ignore first line of csv
        if i == 0:
            continue
        row = line.split(',')
        row[2] = row[2][1:-1]
        try:
            userdata[row[2]].append(row)
        except:
            userdata[row[2]] = row
    conditiondata = {}
    for i, line in enumerate(conditionfile):
        line = line.strip()
        # ignore first line of csv
        if i == 0:
            continue
        row = line.split(',')
        row[1] = row[1][1:-1]
        row[2] = row[2][1:-1]
        try:
            conditiondata[row[1]].append(row)
        except KeyError:
            conditiondata[row[1]] = [row]
    hashdata = {}
    for k, v in list(userdata.items()):
        if k in conditiondata:
            temp = []
            for t in conditiondata[k]:
                temp.append(t[2])
            hashdata[k] = []
            for i in range(len(QI_INDEX)):
                index = QI_INDEX[i]
                hashdata[k].append(v[index])
            hashdata[k].append(temp)
    for k, v in list(hashdata.items()):
        data.append(v)
    userfile.close()
    conditionfile.close()
    return data
