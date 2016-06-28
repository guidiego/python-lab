# coding: utf-8
from heap.unchained import Heap

def test_heap_init():
    heap = Heap()
    assert heap.items == []
    
def test_heap_push():
    heap = Heap()
    pushed_value = 42
    
    heap.push(pushed_value)
    assert heap.items[0] == pushed_value

def test_heap_pop_without_items():
    heap = Heap()
    heap.pop()
    
def test_heap_pop():
    heap = Heap()
    pushed_value = 42
    another_value = 13
    
    heap.push(pushed_value)
    heap.push(another_value)
    
    heap.pop()
    assert heap.items[0] == pushed_value