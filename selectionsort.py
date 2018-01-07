a = list(map(int ,input().split(" ")))
for i in range(len(a)-1):
    s=i;
    for j in range(i,len(a),1):
        if a[s]>a[j]:
            s=j
    if s!=i:
        a[s],a[i]=a[i],a[s]
print(a)