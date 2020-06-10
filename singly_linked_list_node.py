# ListNode class implements a standard linked list functionality

class ListNode:
    # constructor
    def __init__(self, data=0, next=None):
        self.data = data    #store data
        self.next = next    #store reference to the next item
        return
    
    # method to compare the value with the node data
    def hasValue(self, value):
        return self.value == value

    # method to compare equality of two nodes
    def __eq__(self, other):
        a, b = self, other
        # compare each node's value, and progress to the next node
        while a and b:  
            if a.data != b.data:
                return False
            a, b = a.next, b.next
        return a is None and b is None
    
    # returns object representation
    def __repr__(self):
        node = self
        visited = set()
        first = True

        result = ''

        while node:
            if first:
                first = False
            else:
                result += '->'
            
            #if we visited this node, it can be a cyclic list
            if id(node) in visited: 
                if node.next is not node:
                    result += str(node.data)
                    result += '-> ... ->'
                
                result += str(node.data)
                result += '-> ...'
                break
            else:
                result += str(node.data)
                visited.add(id(node))

            node = node.next
        
        return result

    def __str__(self):
        return self.__repr__()
    

def list_size(node):
    result = 0
    visited = set() #use a set to store unique visited nodes

    while node is not None and id(node) not in visited:
        result += 1
        visited.add(id(node))
        node = node.next
    
    return result