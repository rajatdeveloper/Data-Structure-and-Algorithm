tclass Node(object):

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
    def __init__(self, head=None):
        self.head = head

counter = 0

def insertstart(self, data):
    global counter
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
    counter+=1

def insertlast(self,data):
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
        current.set_next(new_node)
    counter+=1

def show(self):
    current = self.head
    while current:
        print(current.get_data())
        current = current.get_next()

def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    return count

def deletestart(self):
    current=self.head
    self.head=current.get_next()
    counter-=1

def deletelast(self):
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
    current=self.head
    if n is 1:
        self.head=current.get_next()
    else:
        for i in range (n-2):
            current = current.get_next()
        currentx=current.get_next()
        current.set_next(currentx.get_next())
    counter -= 1

def deletebyvalue(self,value):
    current = self.head
    currentx = current.get_next()
    if current.get_data() is value:
        self.head = current.get_next()
    else:
        while True:
            if currentx.get_data() is value:
                break
            current= current.get_next()
            currentx = currentx.get_next()
        current.set_next(currentx.get_next())
    counter -= 1

def searchbyvalue(self,value):
    current=self.head
    k=0
    while current:
        if current.get_data() is value:
            print('found')
            k+=1
            break
        current = current.get_next()
    if k is 0:
        print('not found')

def searchbyvaluerecursion(self,value):
    if self is None:
        print('not found')
        return
    if self.get_data() is value :
        print('found')
        return
    return searchbyvaluerecursion(self.get_next(),value)

def searchbypositionstart(self,postn):
    current = self.head
    for i in range (postn-1):
        current = current.get_next()
    print(current.get_data())

def searchbypositionlast(self,postn):
    current = self.head
    currentx = self.head
    for i in range (postn-1):
        currentx = currentx.get_next()
    while currentx.get_next():
        current = current.get_next()
        currentx = currentx.get_next()
    print(current.get_data())

def reverselinkedlist(self):
    current = self.head;
    prev = None
    while current:
        next = current.get_next()
        current.set_next(prev)
        prev = current
        current = next
    self.head = prev

def reverselinkedlistrecursion(self,current):
    if current.get_next() is None:
        self.head = current
        return
    reverselinkedlistrecursion(self,current.get_next())
    currentx = current.get_next()
    currentx.set_next(current)
    current.set_next(None)

def swapping(self,x,y):
    a2 = self.head
    b2 = self.head
    while True:
        if a2.get_data() is x:
            break
        a1 = a2
        a2 = a2.get_next()
    while True:
        if b2.get_data() is y:
            break
        b1 = b2
        b2 = b2.get_next()
    c = a1.get_next()
    a1.set_next(b1.get_next())
    b1.set_next(c)
    c = a2.get_next()
    a2.set_next(b2.get_next())
    b2.set_next(c)

def showforwardrecursion(self,current):
    if current is None:
        return
    print(current.get_data())
    showforwardrecursion(self, current.get_next())

def showbackwardrecursion(self,current):
    if current is None:
        return
    showbackwardrecursion(self, current.get_next())
    print(current.get_data())

def sortedtwolinkedlist(a,b):
    a=a.head
    b=b.head
    if a is None:
        return b
    if b is None:
        return a
    if a and b:
        if a.get_data() <= b.get_data():
            sorting = a
            a=sorting.get_next()
        else:
            sorting = b
            b = sorting.get_next()
    ans = sorting
    while a and b:
        if a.get_data() <= b.get_data():
            sorting.set_next(a)
            sorting = a
            a=sorting.get_next()
        else:
            sorting.set_next(b)
            sorting = b
            b = sorting.get_next()
    if a is None:
        sorting.set_next(b)
    if b is None:
        sorting.set_next(a)
    ans = LinkedList(ans)
    return ans

def cycledetection(self):
    slow = self.head
    fast = self.head
    k=0
    while slow and fast and fast.get_next():
        slow = slow.get_next()
        fast = fast.get_next()
        fast = fast.get_next()
        if (slow == fast):
            print('loop found')
            k+=1
            break
    global loopcount
    while fast:
        loopcount = loopcount+1
        fast = fast.get_next()
        if fast == slow:
            break
    if k == 0:
        print("no loop")
    return

def createcycle(self):
    x = self.head
    for i in range(counter - 1):
        if i < 5:
            y = x
        x = x.get_next()
    x.set_next(y)

def startloop(self):
    slow = self.head
    fast = self.head
    for i in range(loopcount):
        slow = slow.get_next()
    while slow and fast:
        if slow == fast:
            print(slow.get_data())
            break
        slow = slow.get_next()
        fast = fast.get_next()



r=LinkedList()
insertstart(r,119)
insertlast(r,108)
insertlast(r,107)
insertlast(r,106)
insertlast(r,105)
insertlast(r,104)
insertlast(r,103)
insertlast(r,102)
show(r)
reverselinkedlistrecursion(r,r.head)
show(r)