from list_node import ListNode
'''
19. Remove Nth Node From End of List
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
'''

# We need to reduce the number of passes we make
# We use two pointer solution, where first progresses n+1 nodes in front of the second
# then we just relink the second to the next next node
# Time complexity is O(n) where n is the lenght of the linked list
# Space complexity is O(1) since we only used constant extra space


def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode()
    dummy.next = head

    first = head
    for _ in range(n):      #traverse the first pointer n nodes to the front
        first = first.next

    second = dummy
    while first:
        first, second = first.next, second.next
        # second points to the (n+1)-th last node, deletes its successor
    second.next = second.next.next
    return dummy.next

