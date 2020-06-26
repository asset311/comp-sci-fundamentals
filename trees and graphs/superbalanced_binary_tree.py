class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

'''
A tree is 'superbalanced' if the difference between the depths of any two leaf nodes
is no greater than 1.
Write a function to see if a binary tree is 'superbalanced'.
'''
# Time complexity is O(n), space complexity is O(n)
# The function call stack reaches a maximum depth of h, so space complexity is O(h
# The minimum value for h is log(n+1) (complete binary tree) or n (completely skewed tree)
def is_balanced(tree):
    if not tree:
        return True
    
    def find_depth(tree, depths, depth):
        # base case - we are at a leaf node
        if tree:
            if (not tree.left) and (not tree.right):
                if not depth in depths:
                    depths.append(depth)
            else:
                find_depth(tree.left, depths, depth+1)
                find_depth(tree.right, depths, depth+1)

    depths, depth = [], 0
    find_depth(tree, depths, depth)

    if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[-1]) > 1):
        return False
    
    return True


'''
This solution works, but requires visits of all leaf nodes, which may be suboptimal.
We can short-circuit if there are more than two different depths or
if the difference between two different depths is already greater than 1

One tip: Remember that breadth-first uses a queue and depth-first uses a stack (could be the call stack or an actual stack object). 
That's not just a clue about implementation, it also helps with figuring out the differences in behavior. 
Those differences come from whether we visit nodes in the order we see them (first in, first out) or 
we visit the last-seen node first (last in, first out).
'''

def is_balanced_iterative(tree_root):
    if not tree_root:
        return True

    depths = [] 
    nodes = []  # FILO stack, to make sure we visit nodes from the bottom
    nodes.append((tree_root, 0))    #a node is a tuple (node, depth)

    while len(nodes):
        # Pop a node and its depth from the stack of nodes
        node, depth = nodes.pop()

        # Case: we found a leaf node
        if (not node.left) and (not node.right):
            # We only care if it is a new depth
            if depth not in depths:
                depths.append(depth)

                # We can an unbalanced tree in two ways:
                # Either there are more than 2 heights
                # Or the difference between 2 heights is greater than 1
                if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]>1)):
                    return False
        
        # not a leaf node
        else:
            # proceed visiting new nodes
            if node.left:
                nodes.append((node.left, depth+1))
            if node.right:
                nodes.append((node.right, depth + 1))
        
    return True

    
'''
Below are the test cases
'''
# Tests

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

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_both_subtrees_superbalanced_two(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        right = tree.insert_right(4)
        left.insert_left(3)
        left_right = left.insert_right(7)
        left_right.insert_right(8)
        right_right = right.insert_right(5)
        right_right_right = right_right.insert_right(6)
        right_right_right.insert_right(9)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_at_different_levels(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        left_left = left.insert_left(3)
        left.insert_right(4)
        left_left.insert_left(5)
        left_left.insert_right(6)
        right = tree.insert_right(7)
        right_right = right.insert_right(8)
        right_right_right = right_right.insert_right(9)
        right_right_right.insert_right(10)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)