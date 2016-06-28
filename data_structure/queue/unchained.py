# coding: utf-8

class Queue(object):
    def __init__(self):
        self.items = []
        
    def insert(self, item):
        self.items.append(item)
    
    def pop(self):
        if (self.items):
            self.items.pop(0)