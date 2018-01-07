class stack(object):
    def __init__(self,array = []):
        self.a = array

    def push(self,data):
        self.a.append(data)

    def pop(self):
        if r.isempty():
            print("empty")
        else:
            return self.a.pop()

    def isempty(self):
        if self.a == []:
            return True
        else:
            return False

    def show(self):
        print(self.a)

r = stack()
s = input()
x = len(s)
for i in range(x-1,-1,-1):
    if s[i].isdigit():
        r.push(int(s[i]))
    else:
        n1 = r.pop()
        n2 = r.pop()
        if s[i] is '+':
            r.push(n1+n2)
        elif s[i] is '-':
            r.push(n1-n2)
        elif s[i] is '*':
            r.push(n1*n2)
        elif s[i] is '/':
            r.push(n1/n2)
        elif s[i] is '^':
            r.push(n1**n2)
print(r.pop())
