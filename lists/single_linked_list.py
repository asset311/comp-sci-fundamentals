from list_node import ListNode

class SingleLinkedList:

    # initiate an object
    def __init__(self):
        self.head = None
        self.tail = None
        return
    
    # return number of nodes
    def list_length(self):
        node = self.head
        count = 0
        while node:
            count +=1
            node = node.next
        return
    
    # output the node values
    def output_list(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

        return

    # add a node at the end of the list
    def add_list_item(self, item):
        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        
        self.tail = item
        return
    
    # search the list for the nodes with a specified value
    def unordered_search(self, value):
        node = self.head
        node_id = 1
        result = []

        while node:
            if node.data == value:
                result.append(node_id)
            
            node = node.next
            node_id += 1

        return result
    
    # remove the node according to its id
    def remove_list_item_by_id(self, id):
        return
    
