# Implementations of regular stack, and a stack that returns max with O(1) time complexity

class Stack:

    def __init__(self):
        # initialize an empty stack
        self._items = []
    
    
    def empty(self) -> bool:
        return len(self._items) == 0

    def push(self, item) -> None:
        # push a new item onto the stack
        self._items.append(item)
    
    def pop(self, item):
        # remove and return the last item
        # if empty, then throw an exception
        if self.empty():
            raise IndexError ('empty stack')
        
        return self._items.pop()

    def peek(self):
        # returns the last item without removing
        if self.empty():
            return None
        return self._items[-1]



# stack that knows its maximum value
# all operations are of O(1) time complexity
# additional space complexity O(n) regardless of stored keys

from collections import namedtuple
from typing import List

class MaxStackCached:
    # define a new type that holds the element and stack's max
    ItemWithCachedMax = namedtuple('ItemWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._items: List[ItemWithCachedMax] = []
    
    def empty(self) -> bool:
        return len(self._items) == 0
    
    def get_max(self) -> int:
        return self._items[-1].max
    
    def push(self, item: int) -> None:
        # update max on push
        self._items.append(
            self.ItemWithCachedMax(item, item if self.empty() else max(item, self.get_max()))
        )

    #removes and returns the item
    def pop(self) -> int:
        if self.empty():
            raise IndexError('empty stack')
        return self._items.pop().element
    
    #doesn't remove the item
    def peek(self) -> int:
        if self.empty():
            return None
        return self._items[-1].element

# we can reuse regular Stack class and implement MaxStack by having separate stacks
# one for holding the items, and the second for holding maxes
# all operations are O(1) time complexity
# additional space of O(m), where m is the number of operations performed on the stack
class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.maxes_stack = Stack()
    
    def empty(self):
        return self.stack.empty()
    
    def pop(self) -> int:
        # remove and return the item at the top of the stack
        item = self.stack.pop()

        # If it equals the top item in maxes_stack, they must have been pushed
        # in together. So we'll pop it out of maxes_stack too.
        if item == self.maxes_stack.peek():
            self.maxes_stack.pop()
        
        return item

    def push(self, item) -> None:
        # add the item to the top of the stack
        self.stack.push(item)
        
        # if the item is greater or equal to the last item in maxes_stack,
        # this is the new max, so we push onto the maxes_stack
        if self.maxes_stack.peek() is None or item >= self.maxes_stack.peek():
            self.maxes_stack.push(item)
        
    def peek(self) -> int:
        return self.stack.peek()
    
    def get_max(self) -> int:
        # the last item in the maxes_stack is the max in our stack
        return self.maxes_stack.peek()
