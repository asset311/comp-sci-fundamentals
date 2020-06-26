'''
Remove nth element form a list, assuming n is valid (i.e. not larger than the length of the list)
'''

class ListNode:
    # constructor
    def __init__(self, data=0, next=None):
        self.data = data    #store data
        self.next = next    #store reference to the next item
        return


def delete_nth_node(node:ListNode, n:int) -> Node:
    head = tail = node

    if n == 1:
        head = head.next
        return head
    
    i = 0
    while (tail is not None) and i < n-2:
        tail = tail.next
        i += 1
    tail.next = tail.next.next

    return head
    
