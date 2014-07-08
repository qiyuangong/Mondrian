#!/usr/bin/env python
#coding=utf-8

# logic tree
class GenTree(object):

    """Class for Generalization hierarchies (Taxonomy Tree). 
    Store tree node in instances.
    self.value: node value
    self.level: tree level (top is 0)
    self.support: support
    self.parent: ancestor node list
    self.child: direct successor node list
    self.cover: leaves nodes of current node 
    """

    def __init__(self, value = None, parent = None, isleaf=False):
        self.value = ''
        self.level = 0
        self.support = 0
        self.parent = []
        self.child = []
        self.cover = {}
        if value != None:
            self.value = value
        if parent != None:
            self.parent = parent.parent[:]
            self.parent.insert(0, parent)
            parent.child.append(self)
            self.level = parent.level + 1
            for t in self.parent:
                if isleaf:
                    t.cover[self.value] = self
                    t.support += 1
                
    def node(self, value):
        """Search tree with value, return GenTree node.
        return point to that node, or None if not exists
        """
        try:
            return self.cover[value]
        except:
            return None