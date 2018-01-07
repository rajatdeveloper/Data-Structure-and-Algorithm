class Node(object):
    def __init__(self,data=None,left=None,right=None,height = 0):
        self.data = data
        self.left = left
        self.right = right
        self.height = height

class AVL(object):
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

        current.height =1+max(getheight(current.left),getheight(current.right))

        balance = balancefactor(current)

        if balance > 1 and node.data < current.left.data:
            return rightRotate(current)

        if balance < -1 and node.data > current.right.data:
            return leftRotate(current)

        if balance > 1 and data.node > current.left.data:
            current.left = leftRotate(current.left)
            return rightRotate(current)

        if balance < -1 and data.node < current.right.data:
            current.right = rightRotate(current.right)
            return leftRotate(current)
    return current

def leftRotate(self):
    y = self.right
    T2 = y.left
    y.left = self
    self.right = T2
    self.height = 1 + max(getheight(self.left),getheight(self.right))
    y.height = 1 + max(getheight(y.left),getheight(y.right))
    return y

def rightRotate(self):
    y = self.left
    T3 = y.right
    y.right = self
    self.left = T3
    self.height = 1 + max(getheight(self.left),getheight(self.right))
    y.height = 1 + max(getheight(y.left),getheight(y.right))
    return y

def balancefactor(self):
    if self is None:
        return -1
    return getheight(self.left) - getheight(self.right)

def getheight(self):
    if self is None:
        return -1
    return self.height

def inorder(self):
    if self:
        inorder(self.left)
        print(str(self.data)+" " +str(self.height))
        inorder(self.right)

def preorder(self):
    if self:
        print(self.data)
        preorder(self.left)
        preorder(self.right)

r = AVL()
insert(r,r.root,Node(10))
print(r.root.data)
r.root = insert(r,r.root,Node(20))
print(r.root.data)
r.root = insert(r,r.root,Node(30))
print(r.root.data)
r.root = insert(r,r.root,Node(40))
print(r.root.data)
r.root = insert(r,r.root,Node(50))
print(r.root.data)
r.root = insert(r,r.root,Node(25))
print(r.root.data)