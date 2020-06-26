class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class QueueTwoStacks(object):

    def __init__(self):
        self._in_stack = Stack()
        self._out_stack = Stack()
    
    def enqueue(self, item) -> None:
        self._in_stack.push(item)
    
    def dequeue(self):
        if not self._out_stack.peek():
            item = self._in_stack.pop()
            if not item:
                return None
            else:
                 while item:
                    self._out_stack.push(item)
                    item = self._in_stack.pop()

            return self._out_stack.pop()
        return self._out_stack.pop()

# Each enqueue is O(1)
# Total cost for item is O(1), not individual enqueue() and dequeue()
# If we have m enqueues and dequeues this comes to a total of O(m)
    