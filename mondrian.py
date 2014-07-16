#!/usr/bin/env python
#coding=utf-8

from partition import Partition

global_QID_len = 10
global_K = 0
gl_result = []
gl_att_ranges = []


def getNormalizedWidth(partition, index):
    """return Normalized width of partition
    similar to NCP
    """
    width = partition.high - partition.low
    return width / gl_att_ranges[index]



def choose_dimension(partition):
    """chooss dim with largest normWidth
    """
    max_ncp = 0
    max_dim = -1
    for i in range(global_QID_len):
        normWidth = getNormalizedWidth(partition, i)
        if normWidth > max_ncp:
            max_ncp = normWidth
            max_dim = i
    if max_dim != -1:
        return max_dim


def frequency_set(partition, dim):
    """get the frequency_set of partition on dim
    """
    value_set = set()
    frequency = {}
    for record in partition:
        if record[dim] in value_set:
            frequency[record[dim]]++
        else:
            frequency[record[dim]] = 1
    return (value_set, frequency_set)


def find_median(fs):
    """find the middle of the partition, return splitVal
    """
    splitVal = ''
    value_list = fs[0]
    frequency = fs[1]
    total = sum(frequency.keys())
    middle = total / 2
    if middle < global_K:
        return ''
    index = 0
    for t in value_list:
        if index < middle:
            index += frequency[t]
            splitVal = t
            break
    else:
        print "Error: cannot find splitVal"
    return splitVal


def allow_split(partition):
    return True


def anonymize(partition):
    """recursively partition groups until not allowable
    """
    if allow_split(partition) == False:
        gl_result.append(partition)
        return
    dim = choose_dimension(partition)
    fs = frequency_set(partition, dim)
    value_list = list(fs[0])
    sort(value_list, cmp=node_cmp)
    fs[0] = value_list
    splitVal = find_median(fs)
    index = value_list.index(splitVal)

    lhs = Partition()
    rhs = Partition()
    for i, temp in enumerate(partition.member):
        if i <= index:
        # lhs = [low, means]
            lhs.member.append(temp)
        elif:
        # rhs = (means, high)
            rhs.member.append(temp)
    # anonymize sub-partition
    anonymize(lhs)
    anonymize(rhs)


def mondrian():
    """
    """
    global global_K, global_QID_len, gl_result
    anonymize(partition)

    return gl_result