class Node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BST(object):
    def __init__(self,root = None):
        self.root = root

def insert(self,current,node):
    if self.root is None:
        self.root = node
    else:
        if current.data < node.data:
            if current.right is None:
                current.right = node
            else:
                insert(self,current.right, node)
        else:
            if current.left is None:
                current.left = node
            else:
                insert(self,current.left, node)

def inorder(self):
    if self:
        inorder(self.left)
        print(self.data)
        inorder(self.right)

def preorder(self):
    if self:
        print(self.data)
        preorder(self.left)
        preorder(self.right)

def postorder(self):
    if self:
        postorder(self.left)
        postorder(self.right)
        print(self.data)

def search(self, value):
    if self is None:
        print("not found")
        return None
    if self.data is value:
        print("found")
        return self
    if self.data < value:
        return search(self.right, value)
    return search(self.left, value)


def minvalue(self):
    while (self.left is not None):
        self = self.left
    return self

def maxvalue(self):
    while (self.right is not None):
        self = self.right
    return self

def height(self):
    if self is None:
        return -1
    return max(height(self.left),height(self.right)) + 1

def numberofnode(self):
    if self is None:
        return 0
    return (numberofnode(self.left)+numberofnode(self.right)+1)

def deletenode(self, key):
    if self is None:
        return
    if key < self.data:
        self.left = deletenode(self.left, key)
    elif (key > self.data):
        self.right = deletenode(self.right, key)
    else:
        if self.left is None:
            temp = self.right
            self = None
            return temp

        elif self.right is None:
            temp = self.left
            self = None
            return temp
        temp = minvalue(self.right)
        self.data = temp.data
        self.right = deletenode(self.right, temp.data)
    return self

def getsuccessor(self,data):
    self = self.root
    current = search(self,data)
    if current is None:
        return None
    if current.right is not None:
        return minvalue(current.right)
    else:
        successor = None
        ancestor = self
        while(ancestor!=current):
            if current.data < ancestor.data:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor

r = BST()
insert(r,r.root,Node(10))
insert(r,r.root,Node(20))
insert(r,r.root,Node(30))
insert(r,r.root,Node(40))
insert(r,r.root,Node(50))
insert(r,r.root,Node(25))
preorder(r.root)