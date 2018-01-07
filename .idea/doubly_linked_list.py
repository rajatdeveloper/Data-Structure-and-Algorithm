class Node(object):

    def __init__(self, data=None, prev_node=None,next_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def get_prev(self):
        return self.prev_node

    def set_prev(self, new_prev):
        self.prev_node = new_prev

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

counter = 0

def insertstart(self, data):
    global counter
    current=self.head
    new_node = Node(data)
    new_node.set_next(current)
    if counter > 0:
        current.set_prev(new_node)
    self.head = new_node
    counter+=1

def insertlast(self,data):
    global counter
    new_node = Node(data)
    if counter == 0:
        self.head = new_node
    else:
        current = self.head
        while current.get_next():
            current = current.get_next()
        new_node.set_prev(current)
        current.set_next(new_node)
    counter+=1

def insertn(self,data,n):
    global counter
    if n is 1:
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    else:
        current = self.head
        for i in range(n-2):
            current = current.get_next()
        new_node = Node(data)
        new_node.set_next(current.get_next())
        new_node.set_prev(current)
        current.set_next(new_node)
    counter+=1

def deletestart(self):
    global counter
    current=self.head
    self.head=current.get_next()
    if counter > 1:
        current = self.head
        current.set_prev(None)
    counter-=1

def deletelast(self):
   global counter
   current=self.head
   currentx=current.get_next()
   if (currentx==None):
       self.head = None
   else:
        while currentx.get_next():
            current=current.get_next()
            currentx = currentx.get_next()
   current.set_next(None)
   counter -= 1

def deleten(self,n):
    global counter
    current = self.head
    if n is 1:
        self.head = current.get_next()
        if counter > 1:
            current = self.head
            current.set_prev(None)
    else:
        for i in range (n-2):
            current = current.get_next()
        currentx=current.get_next()
        currentx=currentx.get_next()
        current.set_next(currentx)
        if currentx != None:
            currentx.set_prev(current)
    counter -= 1

def show(self):
    current = self.head
    while current:
        print(current.get_data())
        current = current.get_next()

def showbackward(self):
    current = self.head
    while current.get_next():
        current = current.get_next()
    while current:
        print(current.get_data())
        current = current.get_prev()

r=LinkedList()
insertlast(r,11)
insertlast(r,10)
insertlast(r,16)
insertlast(r,19)
insertlast(r,15)
insertlast(r,12)
deletelast(r)
show(r)
showbackward(r)