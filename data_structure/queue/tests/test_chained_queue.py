# coding: utf-8
from queue.chained import ChainedQueue

inserted_value = 42
another_value = 13
some_value = 1

def test_queue_init():
    queue = ChainedQueue()
    assert queue.head == None and queue.tail == None
    
def test_queue_insert():
    queue = ChainedQueue()
    queue.insert(inserted_value)
    
    assert queue.head.value == inserted_value

def test_queue_insert_multi_values():
    queue = ChainedQueue()
    
    queue.insert(inserted_value)
    queue.insert(another_value)
    
    assert queue.head.value == inserted_value and queue.tail.value == another_value

def test_queue_pop_without_items():
    queue = ChainedQueue()
    queue.pop()

def test_queue_pop():
    queue = ChainedQueue()
    
    queue.insert(inserted_value)
    queue.insert(some_value)
    queue.insert(another_value)
    
    queue.pop()
    
    assert queue.head.value == some_value
