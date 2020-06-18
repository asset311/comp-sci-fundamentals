
class BinaryTree(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right



# Preorder traversal - root, left, right
def visitPreorder(node):
    if not node:
        return
    
    print(node.value)
    visitPreorder(node.left)
    visitPreorder(node.right)

def visitPreorderIterative(node):
    nodes = []
    nodes.append(node)
    #because we are using a nodes_to_visit to process nodes, remember that it is FILO
    while nodes:
        node = nodes.pop()
        
        print(node.value, end=' ')

        if node.right:
            nodes.append(node.right)

        if node.left:
            nodes.append(node.left)


# Iorder traversal - left, current node, right
def visitInorder(node):
    if not node:
        return
    
    visitInorder(node.left)

    print(node.value, end=' ')

    visitInorder(node.right)


# sample code, needs more work 
def visitInorderIterative(root):
    visited_nodes = []    
    nodes_to_visit = []  #imitates nodes_to_visit

    current_node = root
    while current_node or nodes_to_visit:
        while current_node:     #terminates when there are no more left children to traverse
            nodes_to_visit.append(current_node)
            current_node = current_node.left
        current_node = nodes_to_visit.pop()
        visited_nodes.append(current_node.value)

        current_node = current_node.right
    
    #print in inorder traversal
    for node in visited_nodes:
        print(node, end=' ')
    

# Postorder traversal - left, right, current node
def visitPostorder(node):
    if not node:
        return
    
    visitPostorder(node.left)
    visitPostorder(node.right)
    print(node.value, end=' ')


# we use two stacks
def visitPostorderIterative(root):
    if not root:
        return
    s1 = []
    s2 = []
    s1.append(root)
    while (s1):
        root = s1.pop()
        s2.append(root)
        if root.left:
            s1.append(root.left)
        if root.right:
            s1.append(root.right)
    
    while s2:
        root = s2.pop()
        print(root.value, end=' ')



tree = BinaryTree('A')
tree.right = BinaryTree('C')
tree.left = BinaryTree('B')
tree.left.left = BinaryTree('D')
tree.left.right = BinaryTree('E')
tree.left.right.left = BinaryTree('F')