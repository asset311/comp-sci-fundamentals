# Given a BST, it is very easy to search it recursively

class BSTNode(object):
    def __init__(self, data = None, left = None, right = None):
        self.data, self.left, self.right = data, left, right 


def search_bst(tree, key):
    return (
        tree if not tree or tree.data == key 
        else search_bst(tree.left, key) if key < tree.data 
        else search_bst(tree.right, key) 
    )

