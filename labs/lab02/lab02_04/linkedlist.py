class Node:
    def __init__(self, data, nextid=None):
        self.data = data
        self.nextid = nextid


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nextid = self.head
            self.head = new_node
        self.size = self.size + 1

    def pop_front(self, data):
        copy_head = self.head




