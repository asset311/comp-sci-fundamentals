'''
Delete a node from a singly-linked list, given only a variable pointing to that node.
Adopted from Interview Cake
'''

class ListNode:
    # constructor
    def __init__(self, data=0, next=None):
        self.data = data    #store data
        self.next = next    #store reference to the next item
        return

# because we do not have a link to previous node, instead of deleting
# we can copy the value from the next node
# and point to the next next node
# this will throw an exception in two cases:
# if it is only one node
# if it is the tail node
def delete_node(node_to_delete):
    # get the input node's next node, the one we want to skip to
    next_node = node_to_delete.next

    if next_node:
        # simply copy and link to the next next node
        node_to_delete.value = node_to_delete.next.value
        node_to_delete.next = node_to_delete.next.next
    else:
        # we throw an exception if we try to delete the last node
        raise Exception("Can't delete the last node with this method")

# Complexity
# Time is O(1)
# Space is O(1)