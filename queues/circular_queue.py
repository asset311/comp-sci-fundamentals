# Circular queue that can be dynamically resized
# Implemented as a fixed array with empty spaces filled with None
# Time complexity of enqueue is O(1)
# Time complexity of dequeue is O(1) since no shifting to the right is required

class Queue:

    SCALE_FACTOR = 2    # double the size every time we need to resize
    def __init__(self, capacity):
         self._entries = [None] * capacity  #fixed size queue initialized with nulls
         self._head = self._tail = self._num_queue_elements = 0 

    
    def enqueue(self,x):
        #queue needs to resize
        if self._num_queue_elements == len(self._entries):
            #makes the queue elements appear consecutively
            self._entries = (
                self._entries[self._head:] + self._entries[:self._head])
            #reset head and tail
            self._head, self._tail = 0, self._num_queue_elements
            self._entries += [None] * (
                len(self._entries) * Queue.SCALE_FACTOR - len(self._entries))
        
        #no resizing needed yet
        self._entries[self._tail] = x
        self._tail = (self._tail + 1) % len(self._entries)  #since it's circular, need to modulo length
        self._num_queue_elements += 1
    
    def dequeue(self):
        if not self._num_queue_elements:
            raise IndexError('empty queue')
        self._num_queue_elements -= 1
        ret = self._entries[self._head]
        self._head = (self._head + 1) % len(self._entries)
    
    def size(self):
        return self._num_queue_elements