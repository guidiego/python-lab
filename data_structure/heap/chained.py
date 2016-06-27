# coding: utf-8

class ChainedHeap(object):
    def __init__(self):
        self.head = None
    
    def push(self, value):
        newItem = HeapItem(value, self.head);
        self.head = newItem
        
    def pop(self):
        self.head = self.head.previous
    
class HeapItem(object):
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous