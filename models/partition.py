#!/usr/bin/env python
#coding=utf-8

# partition for partition based algorithms
class Partition:

    """Class for Group, which is used to keep records 
    Store tree node in instances.
    self.member: records in group
    self.low: lower point 
    self.high: higher point 
    """

    def __init__(self, data):
        self.low = []
        self.high = []
        self.value = []
        self.member = data
        self.splitable = True
