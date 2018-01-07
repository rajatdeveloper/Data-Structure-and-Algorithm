a = list(map(int ,input().split(" ")))
for i in range(len(a)):
    for j in range(i,0,-1):
        if a[j]>=a[j-1]:
            break
        a[j],a[j-1]=a[j-1],a[j]
print(a)