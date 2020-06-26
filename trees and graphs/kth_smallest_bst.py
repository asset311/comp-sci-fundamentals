'''
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
https://leetcode.com/problems/kth-smallest-element-in-a-bst/solution/

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right

# Recursive solution
# Inorder traversal of BST gives sorted list
def kthSmallest(self, root:TreeNode, k:int) -> int:
    stack = []

    while True:
        while root:     # populate with the leftmost subtree
            stack.append(root)
            root = root.left
    
        root = stack.pop()
        k -=1

        # if we're at kth smallest, return the value
        if k == 0:
            return root.val

        root = root.right   # explore the right, if it exists




## RECURSIVE SOLUTION ##
## inorder search on BST will give sorted list ##
def inorder(root):
    if root is None:
        return []
    else:
         return inorder(root.left) + [root.val] + inorder(root.right)

    return inorder(root)[k-1]