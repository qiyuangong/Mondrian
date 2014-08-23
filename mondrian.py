#!/usr/bin/env python
#coding=utf-8

import heapq
import pdb


__DEBUG = True
gl_QI_len = 10
gl_K = 0
gl_result = []
gl_QI_ranges = []
gl_QI_dict = []
gl_QI_order = []


class Partition:

    """Class for Group, which is used to keep records
    Store tree node in instances.
    self.member: records in group
    self.low: lower point
    self.high: higher point
    """

    def __init__(self, data):
        """
        split_tuple = (index, low, high)
        """
        self.low = [10000000000000]*gl_QI_len
        self.high = [-1]*gl_QI_len
        self.allow = [0]*gl_QI_len
        self.member = data[:]
        # if len(split_tuple) > 0:
        #     self.check[split_tuple[0]] = split_tuple[0]
        #     self.low[split_tuple[0]] = split_tuple[1]
        #     self.high = split_tuple[2]
        for temp in self.member:
            for index in range(gl_QI_len):
                pos = gl_QI_dict[index][temp[index]]
                if pos < self.low[index]:
                    self.low[index] = pos
                elif pos > self.high[index]:
                    self.high[index] = pos


def cmp_str(element1, element2):
    """compare number in str format correctley
    """
    return cmp(int(element1), int(element2))


def static_values(data):
    """sort all attributes, get order and range
    """
    att_values = []
    for i in range(gl_QI_len):
        att_values.append(set())
        gl_QI_dict.append({})
    for temp in data:
        for i in range(gl_QI_len):
            att_values[i].add(temp[i])
    for i in range(gl_QI_len):
        value_list = list(att_values[i])
        gl_QI_ranges.append(len(value_list))
        value_list.sort(cmp=cmp_str)
        gl_QI_order.append(value_list[:])
        for index, temp in enumerate(value_list):
            gl_QI_dict[i][temp] = index


def getNormalizedWidth(partition, index):
    """return Normalized width of partition
    similar to NCP
    """
    width = partition.high[index] - partition.low[index]
    return width * 1.0 / gl_QI_ranges[index]


def choose_dimension(partition):
    """chooss dim with largest normWidth
    """
    # max_wi
    max_witdh = -1
    max_dim = -1
    for i in range(gl_QI_len):
        normWidth = getNormalizedWidth(partition, i)
        if normWidth > max_witdh:
            max_witdh = normWidth
            max_dim = i
    # if __DEBUG and max_witdh == 0:
    #     print "all QI values are equal"
    return max_dim


def frequency_set(partition, dim):
    """get the frequency_set of partition on dim
    """
    value_set = set()
    frequency = {}
    for record in partition.member:
        try:
            if record[dim] in value_set:
                frequency[record[dim]] += 1
            else:
                frequency[record[dim]] = 1
                value_set.add(record[dim])
        except:
            pdb.set_trace()
    return frequency


def find_median(frequency):
    """find the middle of the partition, return splitVal
    """
    splitVal = ''
    value_list = frequency.keys()
    value_list.sort(cmp=cmp_str)
    total = sum(frequency.values())
    middle = total / 2
    if middle < gl_K:
        print "Error: size of group less than 2*K"
        return ''
    # if __DEBUG:
    #     print 'total = %d' % total
    #     print 'middle = %d' % middle
    #     pdb.set_trace()
    index = 0
    for t in value_list:
        index += frequency[t]
        if index >= middle:
            splitVal = t
            break
    else:
        print "Error: cannot find splitVal"
    return splitVal


def anonymize(partition):
    """recursively partition groups until not allowable
    """
    if len(partition.member) < 2*gl_K:
        gl_result.append(partition)
        return
    for i in range(gl_QI_len):
        dim = choose_dimension(partition)
        if dim == -1:
            print "Error: dim=-1"
            pdb.set_trace()
        frequency = frequency_set(partition, dim)
        splitVal = find_median(frequency)
        if splitVal == '':
            print "Error: splitVal= null"
            pdb.set_trace()
        middle = gl_QI_dict[dim][splitVal]
        # (dim, partition.low[dim], gl_QI_dict[dim][splitVal])
        lhs = []
        # (dim, gl_QI_dict[dim][splitVal], partition.high[dim]
        rhs = []
        for temp in partition.member:
            pos = gl_QI_dict[dim][temp[dim]]
            if pos <= middle:
                # lhs = [low, means]
                lhs.append(temp)
            else:
                # rhs = (means, high)
                rhs.append(temp)
        if len(lhs) < gl_K or len(rhs) < gl_K:
            partition.allow[dim] = 1
            return
        # anonymize sub-partition
        anonymize(Partition(lhs))
        anonymize(Partition(rhs))
        return
    gl_result.append(partition)


def mondrian(data, K):
    """
    """
    global gl_K, gl_result, gl_QI_len
    gl_QI_len = len(data[0])-1
    gl_K = K
    gl_result = []
    result = []
    data_size = len(data)
    static_values(data)
    partition = Partition(data)
    anonymize(partition)
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
                    temp[index] = '%d,%d' % (gl_QI_order[index][p.low[index]], \
                        gl_QI_order[index][p.high[index]])
                elif type(temp[index]) == str:
                    temp[index] = gl_QI_order[index][p.low[index]] + ',' + \
                        gl_QI_order[index][p.high[index]]
            result.append(temp)
    ncp /= gl_QI_len
    ncp /= data_size
    ncp *= 100
    if __DEBUG:
        print "size of partitions"
        print [len(t.member) for t in gl_result]
        print "NCP = %.2f %%" % ncp
        # pdb.set_trace()
    return result
