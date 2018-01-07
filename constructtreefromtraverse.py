class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BT(object):
    def __init__(self,root = None):
        self.root = root

def buildTree(inOrder, preOrder, inStrt, inEnd):
    if (inStrt > inEnd):
        return None
    child=Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1
    if inStrt == inEnd:
        return child
    inIndex = search(inOrder, inStrt, inEnd, child.data)
    child.left = buildTree(inOrder, preOrder, inStrt, inIndex - 1)
    child.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd)
    return child

def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i
def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print(node.data,)
    printInorder(node.right)
r = BT()
inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']
buildTree.preIndex = 0
r.root = buildTree(inOrder, preOrder, 0, len(inOrder) - 1)
printInorder(r.root)
