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
p = { ')':0, '/':2, '*':2, '+':1, '-':1}
s=input()
f=""
for j in range(len(s)-1,-1,-1):
    i=s[j]
    if i.isalpha():
        f=f+i
    elif i is ')':
        r.push(i)
    elif i is '(':
        x = r.pop()
        while  x != ')' :
            f=f+x
            x = r.pop()
    else:
        while len(r.a)>0 and p[r.a[len(r.a)-1]]>=p[i]:
            f=f+r.pop()
        r.push(i)
while len(r.a):
    f=f+r.pop()
f=f[::-1]
print(f)
