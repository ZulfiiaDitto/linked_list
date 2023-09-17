class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data = elem)
                node = node.next

    def add_first(self, node):
        node.next = self.head # set the head as a second node 
        self.head = node # set head = first node to passing node

    def add_last(self, node):
        if not self.head:
            self.head = node
            return 
        for current_node in self: # this trick will traverse thougth the list and set up last node to the variable current_node
            pass
        current_node.next = node

    def add_after(self, target_node, new_node):
        if not self.head: # if list is empty
            raise Exception('list is empty')
        for node in self:
            if node.data == target_node:
                new_node.next = node.next
                node.next = new_node
                return 
        raise Exception('node is not found')
    
    def add_before(self, target_node, new_node):
        if not self.head:
            raise Exception('list is empty')
        if self.head.data == target_node:
            return self.add_first(new_node)
        
        prev_node = self.head # saving previous head in variable
        for node in self:
            if node.data == target_node:
                prev_node.next = new_node
                new_node.next = node
                return 
            prev_node = node # storing reference of the node we just checked
                
        raise Exception('that data was not found!')


    def remove_node(self, target_node):
        if not self.head:
            raise Exception('list is empty')
        if self.head.data == target_node:
            self.head = self.head.next
            return 
        prev_node = self.head
        for node in self:
            if node.data == target_node:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception('Data does not found')
    
        
    def get(self, position):
        """ implementation of get """
        if not self.head:
            raise Exception('List is empty')
        if position == 0:
            return self.head
        else: 
            count = 0 
            for node in self:
                if count == position:
                    return node.data
                count +=1
            return('The position if out of range')
            
    def reverse(self):
        if not self.head:
            raise Exception("list empty")
        
        # TODO implement th ereverse linked list 
           




            


    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)

        
