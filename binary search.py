a = list(map(int , input().split(" ")))
x =int(input())
n=len(a)
first = 0
last = n-1
while first<=last:
    middle = int((first+last)/2)
    print(first)
    print(last)
    print(middle)
    if a[middle] == x:
        print("found")
        break
    elif a[middle]<x:
        first = middle+1
    else:
        last = middle-1
    if first>last:
        print("not found")
        break
