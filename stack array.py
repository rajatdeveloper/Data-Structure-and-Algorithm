class stack(object):
    def __init__(self,array = []):
        self.a = array

    def push(self,data):
        self.a.append(data)

    def pop(self):
        if r.isempty():
            print("empty")
        else:
            self.a.pop()

    def isempty(self):
        if self.a == []:
            return True
        else:
            return False

    def show(self):
        print(self.a)

r = stack()
