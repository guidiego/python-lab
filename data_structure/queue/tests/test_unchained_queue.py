# coding: utf-8
from queue.unchained import Queue

def test_queue_init():
    queue = Queue()
    assert queue.items == []
    
def test_queue_insert():
    queue = Queue()
    inserted_value = 42
    queue.insert(inserted_value)
    
    assert queue.items[0] == inserted_value

def test_queue_pop_without_items():
    queue = Queue()
    queue.pop()
    
def test_queue_pop():
    queue = Queue()
    
    inserted_value = 42
    another_value = 13
    
    queue.insert(inserted_value)
    queue.insert(another_value)
    
    queue.pop()
    
    assert queue.items[0] == another_value 
    