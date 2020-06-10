import collections
from typing import List

# A stack that includes a max operation, in addition to push and pop
# The max method should return the maximum value stored in the stack

'''
We use an additional variable to store the maximum, and everytime a value is 
 pushed or popped, that variable is updated

Assume we use a single auxiliary variable, M, to record the element that is maximum is the stack.
Updating M on pushes is easy,
M = max(M, e) where e is the value being pushed
Updating M on pop is very time consuming, especially is value being popped is M.
Then we'd need to traverse all existing values and determine the new M.

If we trade time for space, then on each push we can record the previous M, essentially
caching the previous M.
Meaning instead of a global max, remember max of the stack with each element 
'''

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    # implements storage with explicit type checking
    def __init__(self):
        self._element_with_cached_max: List[ElementWithCachedMax] = [] 
    
    def max(self) -> int:
        return self._element_with_cached_max[-1].max

    def empty(self) -> bool:
        return len(self._element_with_cached_max) == 0

    def pop(self) -> int:
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max.pop().element  #uses default -1 index
    
    def push(self, x:int) -> None:
        # update max on push
        self._element_with_cached_max.append(
            self.ElementWithCachedMax( x, x if self.empty() else max(x,self.max()))
        )