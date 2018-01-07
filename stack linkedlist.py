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

class stack(object):
    def __init__(self,head=None):
        self.head = head

counter = 0

def push(self, data):
    global counter
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    counter += 1

def pop(self):
   global counter
   if isempty(self):
       print("stack is empty")
   else:
       current = self.head
       self.head = current.get_next()
   counter -= 1

def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    return count

def isempty(self):
    if self.head is None:
        return True
    else:
        return False

def show(self):
    current = self.head
    while current:
        print(current.get_data())
        current = current.get_next()

r = stack()
show(r)
if isempty(r):
    print("empty")