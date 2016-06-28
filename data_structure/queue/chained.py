# coding: utf-8

class ChainedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, value):
        item = QueueItem(value, None)
        
        if (self.head == None):
            self.head = self.tail = item
        else:
            self.tail.next = item
            self.tail = item
    
    def pop(self):
        if (self.head):
            self.head = self.head.next
        
class QueueItem(object):
    def __init__(self, item, next):
        self.value = item
        self.next = next