'''
Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node 
if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left;
its value is less than or equal to the values of every node to its right.
its children nodes are either valid BST nodes themselves or a null.
'''

# We implement a couple of different ways to show different space complexity

class BST(object):
    
    # constructor with default subtrees
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    # similar to recursive version, except maintain stack ourselves
    # average space is O(log(n)) | time is O(log(n))
    # worst space is O(n) | time is O(n)
    def insert(self, value):
        nodes_to_visit = [self]

        while nodes_to_visit is not None:
            node = nodes_to_visit.pop()

            if value < node.value:
                if node.left is None:
                    node.left = BST(value)              # make sure to exit the loop
                    break
                else:
                    nodes_to_visit.append(node.left)    # will need to go to left subtree

            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    nodes_to_visit.append(node.right)
        
        return self
    
    # No need to maintain a stack
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self  #start at root
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self


    # similar to recursive version, except maintain stack ourselves
    # Average: O(log(n)) time | O(log(n)) space
    # Worst:   O(n) time | O(n) space
    def contains(self, value):
        nodes_to_visit = [self]
        while nodes_to_visit is not None:
            node = nodes_to_visit.pop()
            if value == node.value:
                return True
            elif (value < node.value) and (node.left is not None):
                nodes_to_visit.append(node.left)
            elif (value >= node.value) and (node.right is not None):
                nodes_to_visit.append(node.right)
        return False
    

    # No need to maintain a stack
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:  # depth search
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    

    # when we find a value to remove, we need to replace it with 
    # the smallest value from right subtree (i.e. the left-most value from right subtree)
    # Average: O(log(n)) time | O(1) space
	# Worst: O(n) time | O(1) space
    def remove(self, value, parent = None):
        # Write your code here.
        # Do not edit the return statement of this method.
		if value < self.value:
			if self.left:
				self.left.remove(value, self)
		elif value > self.value:
			if self.right:
				self.right.remove(value, self)
		else:	#we are at the node that needs removal
			#has left and right subtrees, assign the min from right subtree
			if self.left and self.right:
				self.value = self.right.get_min_value()
				self.right.remove(self.value, self)	#right subtree may have this value, remove
			elif not parent:	# when value is root
				if self.left:
					self.value = self.left.value
					self.right = self.left.right
					self.left = self.left.left
				elif self.right:
					self.value = self.right.value
					self.left = self.right.left
					self.right = self.right.right
				else:
					#single node tree, do nothing
					pass
			elif parent.left == self:
				parent.left = self.left if self.left else self.right
			elif parent.right == self:
				parent.right = self.left if self.left else self.right
		
        return self

    # iterative
    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
    
    # recursive
    def get_min_value(self):
        if self.left is None:
            return self.value
        else:
            return self.left.get_min_value()
    



    def insert(self,head,data): 
        item = Node(data)
        if head is None:
            head = Node(data)
        else:
            current = head
            while current is not None:
                if current.next is None:
                    current.next = Node(data)
                    break
                current = current.next
        return head
