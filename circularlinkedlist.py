class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head
        self.last = head

counter = 0

def insertstart(self, data):
    global counter
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    current = self.head
    if current.get_next() is None:
        self.last = new_node
    current = self.last
    current.get_next = self.head

def insertlast(self,data):
    global counter
    new_node = Node(data)
    current = self.last
    if self.head is None:
        self.head = new_node
    else:
        current.set_next(new_node)
    self.last = new_node
    new_node.set_next(self.head)
    counter+=1

def show(self):
    current = self.head
    while current:
        print(current.get_data())
        current = current.get_next()

r = LinkedList()
insertstart(r,7)
insertstart(r,6)
insertstart(r,5)
show(r)



