from list_node import ListNode

'''
7.1 Merge two sorted lists
Consider two singly linked lists in which each node holds a number. 
Assume the lists are sorted, i.e., numbers in the lists appear in ascending order within each list. 
The merge of the two lists is a list consisting of the nodes of the two lists in which numbers appear in ascending order
'''

# naive approach is to just merge two lists and then sort
# this does not take into account that both lists are sorted
# time complexity is that of regular sorting, which O(nlog(n))
# a better approach to traverse the two lists, always choosing the node containing the smaller value

def merge_two_sorted_lists(L1: ListNode, L2: ListNode) -> ListNode:
    head = tail = ListNode()    #dummy head points to the original tail

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next
    
    #append the remaining nodes of L1 or L2
    tail.next = L1 or L2

    return head.next

'''
7.4 Test for overlapping lists - lists are cycle-free

Write a Program that takes two cycle-free singly linked lists, 
and determines if there exists a node that is common to both lists.
'''

# brute-force is to store one list's nodes in a hash table, and then iterate through
# the nodes of the other, testing for the presence in the hash table
# time complexity is O(n) and space complexity is O(n) where n is the total number of nodes
def overlapping_no_cycle_lists_naive(L1: ListNode, L2: ListNode):
    L1_nodes = set()
    while L1:
        L1_nodes.add(L1.data)
        L1 = L1.next
    
    while L2:
        if L2.data in L1_nodes:
            return True
        else:
            L2 = L2.next
    
    return False


# a better approach to save space complexity of O(n) is to traverse two lists
# using two nested loops, one iterating through the first list,
# and the other to search the second for the node being processed in the first list
# time complexity is O(n^2)

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    
    l0_len, l1_len = length(l0), length(l1)
    if l0_len > l1_len:
        l0, l1 = l1, l0 #l1 is the longer list
    
    for _ in range(abs(l1_len - l0_len)):
        l1 = l1.next
    
    while l0 and l1 and l1 is not l0:
        l0, l1 = l0.next, l1.next
    
    return l0   # None implies there is no overlap between l0 and l1.

'''
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

l0 = n1
l0.next = n2
l0.next.next = n3
l0.next.next.next = n4
l0.next.next.next.next = n5

l1 = n5
l1.next = n6
l1.next.next = n3
'''

'''
Remove nth element form a list, assuming n is valid (i.e. not larger than the length of the list)
'''
# if we want to make sure that n is not larger than the length of the list, we'd need to know its length
# this guarantees that n is always valid

def remove_nth_element(l:ListNode, n) -> ListNode:
    head = tail = l

    if n == 1:
        head = head.next
        return head

    i = 0
    while tail and i<n-2:
        tail = tail.next
        i += 1
    
    tail.next = tail.next.next

    return head


'''
7.6 Delete a node from a singly-linked list
'''
# Instead of traversing from the head to find the node and then update it's predecessor's next pointer
# Time complexity is O(1)
# Assumes node to delete is not tail
def delete_from_list(node_to_delete: ListNode):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next

'''
7.7 Remove the kth last element from a list, i.e. remove the kth node from the end of list and return its head
'''
# Assumes that k is always valid

