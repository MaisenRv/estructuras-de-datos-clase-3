from Nodes.Node import Node

class Linked_list:
    def __init__(self, node:any = None) -> None:
        self.head = None
        self.tail = None

        if node:
            self.head = node
            self.tail = node
    
    def draw(self):
        self.head.draw()

    def add_end(self, new_node:Node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
