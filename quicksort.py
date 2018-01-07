def quicksort(a,start,end):
    if start<end:
        partitionindex = partition(a,start,end)
        quicksort(a,start,partitionindex-1)
        quicksort(a,partitionindex+1,end)

def partition(a,start,end):
    pivot = a[end]
    partitionindex = start
    for i in range(start,end,1):
        if a[i]<=pivot:
            a[i],a[partitionindex] = a[partitionindex],a[i]
            partitionindex+=1
    a[end],a[partitionindex]=a[partitionindex],a[end]
    return partitionindex
a = list(map(int ,input().split(" ")))
quicksort(a,0,len(a)-1)
print(a)




