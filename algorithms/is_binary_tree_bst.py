'''
Test if a binary tree satisfies the BST property.
Write a program that takes as input a binary tree and checks if the tree satisfies the BST property.
Note that BST property is global.
'''

# It is not sufficient to traverse the tree and check that left and right subtree satisfy the property
# Every node to the left of current node if smaller
# Every node to the right of current node is larger

# Instead of comparing to the sequence of ancestors, we can enforce upper and lower bounds

def is_binary_tree_bst_iterative(root):
    nodes_and_bounds_stack = [(root, -float('inf'), float('inf'))]

    # depth-first search 
    while len(nodes_and_bounds_stack):

        node, lower_bound, upper_bound = nodes_and_bounds_stack.pop()

        # if the node is not in the right place, not a valid BST
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False

        if node.left:
            nodes_and_bounds_stack.append(node.left, lower_bound, node.value)
        
        if node.right:
            nodes_and_bounds_stack.append(node.right, node.value, upper_bound)
    
    return True

def is_binary_tree_bst_recursive(tree, lower_bound = -float('inf'), upper_bound = float('inf')):
    if not tree:
        True    # base case

    elif not lower_bound <= tree.data <= upper_bound:
        return False

    return (is_binary_tree_bst_recursive(tree.left, lower_bound, tree.data) and 
            is_binary_tree_bst_recursive(tree.right, tree.data, upper_bound)) 