#!/usr/bin/env python
# coding=utf-8
from mondrian import mondrian
from utils.read_data import read_data
import sys, copy, random
import pdb


def get_result_one(data, K=10):
    "run mondrian for one time, with k=10"
    print "K=%d" % K
    data_back = copy.deepcopy(data)
    result, eval_result = mondrian(data, K)
    data = copy.deepcopy(data_back)
    print "NCP %0.2f" % eval_result[0] + "%"
    print "Running time %0.2f" % eval_result[1] + "seconds"


def get_result_K(data):
    """
    change K, whle fixing QD and size of dataset
    """
    data_back = copy.deepcopy(data)
    for K in range(5, 55, 5):
        print '#' * 30
        print "K=%d" % K
        result, eval_result = mondrian(data, K)
        data = copy.deepcopy(data_back)
        print "NCP %0.2f" % eval_result[0] + "%"
        print "Running time %0.2f" % eval_result[1] + "seconds"


def get_result_dataset(data, K=10, n=10):
    """
    fix k and QI, while changing size of dataset
    n is the proportion nubmber.
    """
    data_back = copy.deepcopy(data)
    length = len(data_back)
    print "K=%d" % K
    joint = 5000
    h = length / joint
    if length % joint == 0:
        h += 1
    for i in range(1, h + 1):
        pos = i * joint
        ncp = rtime = 0
        if pos > length:
            continue
        print '#' * 30
        print "size of dataset %d" % pos
        for j in range(n):
            temp = random.sample(data, pos)
            result, eval_result = mondrian(temp, K)
            ncp += eval_result[0]
            rtime += eval_result[1]
            data = copy.deepcopy(data_back)
        ncp /= n
        rtime /= n
        print "Average NCP %0.2f" % ncp + "%"
        print "Running time %0.2f" % rtime + "seconds"
        print '#' * 30


def get_result_QI(data, K=10):
    """
    change nubmber of QI, whle fixing K and size of dataset
    """
    data_back = copy.deepcopy(data)
    ls = len(data[0])
    for i in reversed(range(1, ls)):
        print '#' * 30
        print "Number of QI=%d" % i
        result, eval_result = mondrian(data, K, i)
        data = copy.deepcopy(data_back)
        print "NCP %0.2f" % eval_result[0] + "%"
        print "Running time %0.2f" % eval_result[1] + "seconds"


if __name__ == '__main__':
    flag = ''
    len_argv = len(sys.argv)
    try:
        flag = sys.argv[1]
    except:
        pass
    K = 10
    # read record
    data = read_data()
    if flag == 'k':
        get_result_K(data)
    elif flag == 'qi':
        get_result_QI(data)
    elif flag == 'data':
        get_result_dataset(data)
    elif flag == 'one':
        if len_argv > 2:
            K = int(sys.argv[2])
            get_result_one(data, K)
        else:
            get_result_one(data)
    elif flag == '':
        get_result_one(data)
    else:
        print "Usage: python anonymizer [k | qi |data | one]"
    # anonymized dataset is stored in result
    print "Finish Mondrian!!"
