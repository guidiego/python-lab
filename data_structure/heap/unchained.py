# coding: utf-8

class Heap(object):
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items :
            self.items.pop()