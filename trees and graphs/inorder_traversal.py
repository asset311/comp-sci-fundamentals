
# There are two ways to imlement any tree traversal - recursive or iterative
# Inorder traversal - left, current node, right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time is O(N) and space O(N) where N is the number of nodes in the tree
def inorder_recursive(root: TreeNode, array):
    if not root:
        return
    inorder_recursive(root.left, array)
    array.append(root.val)
    inorder_recursive(root.right, array)

# Time is O(h) and space(h) where h is the height of the tree
def inorder_iterative(root:TreeNode, array):
    
    def left_most_inorder(root: TreeNode, stack):
        while root:
            stack.append(root)
            root = root.left
    
    # custom stack to maintain visited nodes
    stack = []

    left_most_inorder(root, stack)
    while stack:
        node = stack.pop()
        if node.right:
            left_most_inorder(node.right, stack)
        array.append(node.val)





# Test tree
root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)