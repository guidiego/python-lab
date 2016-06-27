# coding: utf-8
from heap.chained import ChainedHeap, HeapItem

def test_chained_heap_init():
    heap = ChainedHeap()
    assert heap.head == None
    
def test_chained_heap_push():
    heap = ChainedHeap()
    pushed_value = 42
    
    heap.push(pushed_value)
    assert heap.head.value == pushed_value

def test_chained_heap_pop():
    heap = ChainedHeap()
    pushed_value = 42
    another_value = 13
    
    heap.push(pushed_value)
    heap.push(another_value)
    
    heap.pop()
    assert heap.head.value == pushed_value