class MaxHeap(object):
    def __init__(self):
        self.heap = []
    def parent(self, i):
        return int((i - 1) / 2)
    def heapsize(self):
        return len(self.heap)

def insert(self,data):
    i = r.heapsize()
    self.heap.append(data)
    while (i != 0 and self.heap[self.parent(i)] < self.heap[i]):
        self.heap[self.parent(i)],self.heap[i] = self.heap[i],self.heap[self.parent(i)]
        i = self.parent(i)

def deletemax(self):
    x=self.heapsize()
    self.heap[0],self.heap[x-1] = self.heap[x-1],self.heap[0]
    self.heap.pop()
    heapify(self,0)

def heapify(self,i) :
    x=self.heapsize()
    while (2*i) + 2 < x :
        if self.heap[i] >= self.heap[(2*i)+2] and self.heap[i] >= self.heap[(2*i)+1] :
            break002

        if self.heap[(2*i)+2] > self.heap[(2*i)+1]:
            self.heap[(2*i)+2], self.heap[i] = self.heap[i], self.heap[(2*i)+2]
            i = (2*i)+2
        else:
            self.heap[(2*i)+1], self.heap[i] = self.heap[i], self.heap[(2*i)+1]
            i = (2*i)+1
    if (2 * i) + 1 < x and self.heap[i] < self.heap[(2*i) + 1]:
        self.heap[(2 * i) + 1], self.heap[i] = self.heap[i], self.heap[(2 * i) + 1]


def decreasekey(self, i, k):
    self.heap[i] = k
    while (i != 0 and self.heap[self.parent(i)] < self.heap[i]):
        self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
        i = self.parent(i)


def delete(self, data):
    x = self.heapsize()
    for i in range(x):
        if self.heap[i] == data:
            break
    decreasekey(self, i, float("inf"))
    deletemax(self)

def maxvalue(self):
    print(self.heap[0])

def printheap(self):
    print(self.heap)

r = MaxHeap()
insert(r,18)
insert(r,21)
insert(r,65)
insert(r,63)
insert(r,75)
insert(r,36)
insert(r,70)
insert(r,89)
insert(r,90)
printheap(r)
delete(r,75)
printheap(r)
