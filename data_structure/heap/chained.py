# coding: utf-8

class ChainedHeap(object):
    def __init__(self):
        self.head = None
    
    def push(self, value):
        item = HeapItem(value, self.head)
        self.head = item
        
    def pop(self):
        if self.head :
            self.head = self.head.previous
    
class HeapItem(object):
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous