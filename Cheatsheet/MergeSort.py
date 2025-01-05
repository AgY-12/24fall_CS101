def MergeSort(arr):
    if len(arr)<=1: return arr
    else:
        l,r=arr[:len(arr)//2],arr[len(arr)//2:]
        return Merge(MergeSort(l),MergeSort(r))
def Merge(l,r):
    res=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1
    res+=l[i:]+r[j:]
    return res
print(MergeSort([5,3,7,2,6,9,1,8,4,2,6]))
