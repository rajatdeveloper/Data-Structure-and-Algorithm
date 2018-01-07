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

class queue(object):
    def __init__(self,head=None):
        self.head = head

counter = 0

def enqueue(self, data):
    global counter
    new_node = Node(data)
    current = self.head
    if current is None:
        self.head = new_node
    else:
        current = self.head
        while current.get_next():
            current = current.get_next()
        current.set_next(new_node)
    counter += 1

def dqueue(self):
   global counter
   if isempty(self):
       print("queue is empty")
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

r = queue()
enqueue(r,5)
enqueue(r,6)
enqueue(r,7)
dqueue(r)
dqueue(r)
dqueue(r)
dqueue(r)
show(r)
if isempty(r):
    print("empty")