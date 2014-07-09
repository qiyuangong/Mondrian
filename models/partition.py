#!/usr/bin/env python
#coding=utf-8

# partition for partition based algorithms
class Partition:

    """Class for Group, which is used to keep records 
    Store tree node in instances.
    self.member: records in group
    self.value: group value
    """

    def __init__(self, data, value = ['*'], level = []):
        self.split_list = []
        self.member = data
        self.value = value[:]
        self.splitable = True

    def merge_group(self, guest, middle):
        "merge guest into hostgourp"
        while guest.member:
            temp = guest.member.pop()
            self.member.append(temp)
        self.value = middle[:]

    def merge_record(self, rtemp, middle):
        "merge record into hostgourp"
        self.member.append(rtemp)
        self.value = middle[:]