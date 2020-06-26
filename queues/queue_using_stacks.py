'''
232. Implement Queue using Stacks
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.

'''
class MyQueue:
    
    def __init__(self):
        self._push_stack = []
        self._pop_stack = []
        

    def push(self, x: int) -> None:
        self._push_stack.append(x)
        

    def pop(self) -> int:
        if len(self._pop_stack) == 0:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())
                
        return self._pop_stack.pop()
        

    def peek(self) -> int:
        if len(self._pop_stack) == 0:
            while self._push_stack:
                self._pop_stack.append(self._push_stack.pop())
        return self._pop_stack[-1]
        

    def empty(self) -> bool:
        return (not self._push_stack) and (not self._pop_stack)


'''
COMPLETE THIS SOLUTION
'''