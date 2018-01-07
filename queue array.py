class queue(object):
    def __init__(self,array = []):
        self.a = array

    def enqueue(self,data):
        self.a.append(data)

    def dequeue(self):
        if r.isempty():
            print("empty")
        else:
            self.a.pop(0)

    def isempty(self):
        if self.a == []:
            return True
        else:
            return False

    def show(self):
        print(self.a)

r = queue([4])
r.enqueue(5)
r.enqueue(6)
r.enqueue(7)
print(r.a)