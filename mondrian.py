#!/usr/bin/env python
# coding=utf-8

# Implemented by Qiyuan Gong
# qiyuangong@gmail.com
# 2014-09-11

# @InProceedings{LeFevre2006,
#   Title                    = {Mondrian Multidimensional K-Anonymity},
#   Author                   = {LeFevre, Kristen and DeWitt, David J. and Ramakrishnan, Raghu},
#   Booktitle                = {ICDE '06: Proceedings of the 22nd International Conference on Data Engineering},
#   Year                     = {2006},
#   Address                  = {Washington, DC, USA},
#   Pages                    = {25},
#   Publisher                = {IEEE Computer Society},
#   Doi                      = {http://dx.doi.org/10.1109/ICDE.2006.101},
#   File                     = {:All paper\\Mondrian Multidimensional K-Anonymity_ICDE2006.pdf:PDF},
#   ISBN                     = {0-7695-2570-9},
# }

import pdb
import time


# warning all these variables should be re-inited, if
# you want to run mondrian with different parameters
__DEBUG = False
gl_QI_len = 10
gl_K = 0
gl_result = []
gl_QI_ranges = []
gl_QI_dict = []
gl_QI_order = []


class Partition:

    """
    Class for Group (or EC), which is used to keep records
    self.member: records in group
    self.low: lower point, use index to avoid negative values
    self.high: higher point, use index to avoid negative values
    """

    def __init__(self, data, low, high):
        """
        split_tuple = (index, low, high)
        """
        self.low = low[:]
        self.high = high[:]
        # We found that allow should not be inherited
        # in any case (both numeric and catogoric), or
        # some group will not be well splited.
        self.allow = [1] * gl_QI_len
        self.member = data[:]


def cmp_str(element1, element2):
    """
    compare number in str format correctley
    """
    try:
        return cmp(int(element1), int(element2))
    except:
        return cmp(element1, element2)


def static_values(data):
    """
    sort all attributes, get order and range
    """
    global gl_QI_dict, gl_QI_ranges, gl_QI_order
    # init global variables, or these values may be wrong
    gl_QI_dict = []
    gl_QI_order = []
    gl_QI_ranges = []
    att_values = []
    for i in range(gl_QI_len):
        att_values.append(set())
        gl_QI_dict.append({})
    for temp in data:
        for i in range(gl_QI_len):
            att_values[i].add(temp[i])
    for i in range(gl_QI_len):
        value_list = list(att_values[i])
        value_list.sort(cmp=cmp_str)
        # gl_QI_ranges.append(len(value_list))
        gl_QI_ranges.append(float(value_list[-1]) - float(value_list[0]))
        gl_QI_order.append(list(value_list))
        for index, temp in enumerate(value_list):
            gl_QI_dict[i][temp] = index


def getNormalizedWidth(partition, index):
    """
    return Normalized width of partition
    similar to NCP
    """
    d_order = gl_QI_order[index]
    width = float(d_order[partition.high[index]]) - float(d_order[partition.low[index]])
    return width * 1.0 / gl_QI_ranges[index]


def choose_dimension(partition):
    """
    chooss dim with largest normWidth from all attributes.
    This function can be upgraded with other distance function.
    """
    max_width = -1
    max_dim = -1
    for i in range(gl_QI_len):
        if partition.allow[i] == 0:
            continue
        normWidth = getNormalizedWidth(partition, i)
        if normWidth > max_width:
            max_width = normWidth
            max_dim = i
    if max_width > 1:
        pdb.set_trace()
    return max_dim


def frequency_set(partition, dim):
    """
    get the frequency_set of partition on dim
    """
    frequency = {}
    for record in partition.member:
        try:
            frequency[record[dim]] += 1
        except:
            frequency[record[dim]] = 1
    return frequency


def find_median(frequency):
    """
    find the middle of the partition, return splitVal
    """
    splitVal = ''
    nextVal = ''
    value_list = frequency.keys()
    value_list.sort(cmp=cmp_str)
    total = sum(frequency.values())
    middle = total / 2
    if middle < gl_K:
        print "Error: size of group less than 2*K"
        return ('', '')
    index = 0
    split_index = 0
    for i, t in enumerate(value_list):
        index += frequency[t]
        if index >= middle:
            splitVal = t
            split_index = i
            break
    else:
        print "Error: cannot find splitVal"
    try:
        nextVal = value_list[split_index + 1]
    except:
        nextVal = ''
    return (splitVal, nextVal)


def anonymize(partition):
    """
    recursively partition groups until not allowable
    """
    if len(partition.member) < 2 * gl_K:
        gl_result.append(partition)
        return
    allow_count = sum(partition.allow)
    # only run allow_count times
    for index in range(allow_count):
        # choose attrubite from domain
        plow = partition.low
        phigh = partition.high
        dim = choose_dimension(partition)
        if dim == -1:
            print "Error: dim=-1"
            pdb.set_trace()
        # use frequency set to get median
        frequency = frequency_set(partition, dim)
        (splitVal, nextVal) = find_median(frequency)
        if splitVal == '' or nextVal == '':
            partition.allow[dim] = 0
            continue
        # split the group from median
        mean = gl_QI_dict[dim][splitVal]
        lhigh = phigh[:]
        rlow = plow[:]
        lhigh[dim] = mean
        rlow[dim] = gl_QI_dict[dim][nextVal]
        lhs = []
        rhs = []
        for temp in partition.member:
            pos = gl_QI_dict[dim][temp[dim]]
            if pos <= mean:
                # lhs = [low, mean]
                lhs.append(temp)
            else:
                # rhs = (mean, high]
                rhs.append(temp)
        if len(lhs) < gl_K or len(rhs) < gl_K:
            partition.allow[dim] = 0
            continue
        # anonymize sub-partition
        anonymize(Partition(lhs, plow, lhigh))
        anonymize(Partition(rhs, rlow, phigh))
        return
    gl_result.append(partition)


def mondrian(data, K, QI_num=-1):
    """
    main function of mondrian
    """
    global gl_K, gl_result, gl_QI_len
    # initialization
    if QI_num <= 0:
        gl_QI_len = len(data[0]) - 1
    else:
        gl_QI_len = QI_num
    gl_K = K
    gl_result = []
    result = []
    data_size = len(data)
    static_values(data)
    low = [0] * gl_QI_len
    high = [(len(t) - 1) for t in gl_QI_order]
    partition = Partition(data, low, high)
    # begin mondrian
    start_time = time.time()
    anonymize(partition)
    rtime = float(time.time() - start_time)
    # generalization result and
    # evaluation information loss
    ncp = 0.0
    for p in gl_result:
        rncp = 0.0
        for index in range(gl_QI_len):
            rncp += getNormalizedWidth(p, index)
        rncp *= len(p.member)
        ncp += rncp
        for temp in p.member:
            for index in range(gl_QI_len):
                if type(temp[index]) == int:
                    temp[index] = '%d,%d' % (gl_QI_order[index][p.low[index]],
                                             gl_QI_order[index][p.high[index]])
                elif type(temp[index]) == str:
                    temp[index] = gl_QI_order[index][p.low[index]] + ',' + gl_QI_order[index][p.high[index]]
            result.append(temp)
    # If you want to get NCP values instead of percentage
    # please remove next three lines
    ncp /= gl_QI_len
    ncp /= data_size
    ncp *= 100
    if __DEBUG:
        print "K=%d" % gl_K
        print "size of partitions=%d" % len(gl_result)
        # print [len(t.member) for t in gl_result]
        print "NCP = %.2f %%" % ncp
        # pdb.set_trace()
    return (result, (ncp, rtime))
