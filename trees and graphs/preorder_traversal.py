# There are two ways to imlement any tree traversal - recursive or iterative
# Preorder traversal - current node, left, right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity is O(N) and space O(N) where N is the number of nodes
def preorder_recursive(root:TreeNode, array):
    if not root:
        return
    
    array.append(root.val)
    preorder_recursive(root.left, array)
    preorder_recursive(root.right, array)


def preorder_iterative(root:TreeNode, array):
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        array.append(node.val)

        # push to the stack in the opposite order right, then left subtrees
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# Test 
array = []
root = TreeNode(6)
root.left = TreeNode(4)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(10)
root.right.left = TreeNode(8)
root.right.right = TreeNode(12)

Output: [6, 4, 2, 5, 10, 8, 12]