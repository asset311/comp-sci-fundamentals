'''
Test if a binary tree is height-balanced.
A general definition: 
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of its left and right subtrees is at most one

A better definition is that a tree is balanced if:
1) The height of its left and right subtree differ by at most 1
2) Both substrees are also balanced

We can see that we can have a recursive check that operates on subtrees.
We can also see that as soon as we see an unbalanced subtree, we can terminate our function

Write a function that takes as input the root of binary tree and checks whether the tree is height-balanced.
'''

from collections import namedtuple
def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    # implement a classic postorder traversal - left, current, right
    def check_balanced(tree):
        # base case is leaf node, which is balanced
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        # visit left subtree
        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            #left subtree is not balanced
            return BalancedStatusWithHeight(False, 0)
        
        # visit right subtree
        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            #right subtree is not balanced
            return BalancedStatusWithHeight(False, 0)
        
        # visit current node
        is_balanced = abs(left_result.height - right_result.height) <=1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)
    
    return check_balanced(tree).balanced



