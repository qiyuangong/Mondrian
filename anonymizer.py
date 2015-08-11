"""
run mondrian with given parameters
"""

# !/usr/bin/env python
# coding=utf-8
from mondrian import mondrian
from utils.read_adult_data import read_data as read_adult
from utils.read_informs_data import read_data as read_informs
import sys, copy, random

DATA_SELECT = 'a'


def get_result_one(data, k=10):
    """
    run mondrian for one time, with k=10
    """
    print "K=%d" % k
    data_back = copy.deepcopy(data)
    _, eval_result = mondrian(data, k)
    data = copy.deepcopy(data_back)
    print "NCP %0.2f" % eval_result[0] + "%"
    print "Running time %0.2f" % eval_result[1] + " seconds"


def get_result_k(data):
    """
    change k, whle fixing QD and size of dataset
    """
    data_back = copy.deepcopy(data)
    for k in range(5, 105, 5):
        print '#' * 30
        print "K=%d" % k
        result, eval_result = mondrian(data, k)
        data = copy.deepcopy(data_back)
        print "NCP %0.2f" % eval_result[0] + "%"
        print "Running time %0.2f" % eval_result[1] + " seconds"


def get_result_dataset(data, k=10, num_test=10):
    """
    fix k and QI, while changing size of dataset
    num_test is the test nubmber.
    """
    data_back = copy.deepcopy(data)
    length = len(data_back)
    joint = 5000
    dataset_num = length / joint
    if length % joint == 0:
        dataset_num += 1
    for i in range(1, dataset_num + 1):
        pos = i * joint
        ncp = rtime = 0
        if pos > length:
            continue
        print '#' * 30
        print "size of dataset %d" % pos
        for j in range(num_test):
            temp = random.sample(data, pos)
            _, eval_result = mondrian(temp, k)
            ncp += eval_result[0]
            rtime += eval_result[1]
            data = copy.deepcopy(data_back)
        ncp /= num_test
        rtime /= num_test
        print "Average NCP %0.2f" % ncp + "%"
        print "Running time %0.2f" % rtime + " seconds"
        print '#' * 30


def get_result_qi(data, k=10):
    """
    change nubmber of QI, whle fixing k and size of dataset
    """
    data_back = copy.deepcopy(data)
    num_data = len(data[0])
    for i in reversed(range(1, num_data)):
        print '#' * 30
        print "Number of QI=%d" % i
        _, eval_result = mondrian(data, k, i)
        data = copy.deepcopy(data_back)
        print "NCP %0.2f" % eval_result[0] + "%"
        print "Running time %0.2f" % eval_result[1] + " seconds"


if __name__ == '__main__':
    FLAG = ''
    LEN_ARGV = len(sys.argv)
    try:
        DATA_SELECT = sys.argv[1]
        FLAG = sys.argv[2]
    except IndexError:
        pass
    GL_K = 10
    # read record
    if DATA_SELECT == 'i':
        print "INFORMS data"
        DATA = read_informs()
    else:
        print "Adult data"
        DATA = read_adult()
    if FLAG == 'k':
        get_result_k(DATA)
    elif FLAG == 'qi':
        get_result_qi(DATA)
    elif FLAG == 'data':
        get_result_dataset(DATA)
    elif FLAG == 'one':
        if LEN_ARGV > 2:
            GL_K = int(sys.argv[3])
            get_result_one(DATA, GL_K)
        else:
            get_result_one(DATA)
    elif FLAG == '':
        get_result_one(DATA)
    else:
        print "Usage: python anonymizer [a | i] [k | qi |data | one]"
        print "a: adult dataset, 'i': INFORMS ataset"
        print "k: varying k, qi: varying qi numbers, \
               data: varying size of dataset, one: run only once"
    # anonymized dataset is stored in result
    print "Finish Mondrian!!"
