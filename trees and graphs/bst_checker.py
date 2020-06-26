'''
Implement a function to check that a binary tree is a valid binary search tree

Definitions:
A binary tree is a tree where every node has two or fewer children. The children are usually called left and right.
A binary search tree (BST) is a binary tree where nodes are ordered in a specific way.
The nodes to the left are smaller than the current node
The nodes to the right are larger than the current node

What makes a given node "correct" relative to its ancestors in a BST? Two things:

if a node is in the ancestor's left subtree, then it must be less than the ancestor, and
if a node is in the ancestor's right subtree, then it must be greater than the ancestor.

'''
def is_binary_search_tree(root):
    # start at the root, with arbitrarily small lower bound and large upper bound
    node_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first search
    while len(node_and_bounds_stack):

        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        # if the node isn't in the right place, return straight away
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False
        
        if node.left:
            # this node must be less than the current node
            node_and_bounds_stack.append((node, lower_bound, node.value))
        
        if node.right:
            # this node must be greater than the current node
            node_and_bounds_stack.append((node, node.value, upper_bound))
        
        # if none of the nodes were invalid, return true
        # at this point we checked all the nodes
    return True

# instead of iteratively checking, we can use a recursive function
# and use the call stack
def is_binary_search_tree_recursive(root, lower_bound = -float('inf'), upper_bound = float('inf')):

    # base case
    if not root:
        return True
    
    if (root.value >= upper_bound) or (root.value <= lower_bound):
        return False
    
    return (is_binary_search_tree_recursive(root.left, lower_bound, root.value) and 
            is_binary_search_tree_recursive(root.right, root.value, upper_bound))
    
# O(n) time and O(n) space complexities

'''
Tests
'''
import unittest
class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_valid_full_tree(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(70)
        left.insert_left(10)
        left.insert_right(40)
        right.insert_left(60)
        right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_both_subtrees_valid(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(30)
        right = tree.insert_right(80)
        left.insert_left(20)
        left.insert_right(60)
        right.insert_left(70)
        right.insert_right(90)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_descending_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        left = tree.insert_left(40)
        left_left = left.insert_left(30)
        left_left_left = left_left.insert_left(20)
        left_left_left.insert_left(10)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)

    def test_out_of_order_linked_list(self):
        tree = Test.BinaryTreeNode(50)
        right = tree.insert_right(70)
        right_right = right.insert_right(60)
        right_right.insert_right(80)
        result = is_binary_search_tree(tree)
        self.assertFalse(result)

    def test_one_node_tree(self):
        tree = Test.BinaryTreeNode(50)
        result = is_binary_search_tree(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)