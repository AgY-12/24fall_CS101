def quickSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=arr[len(arr)//2]
        l,m,r=[],[],[]
        for i in arr:
            if i < mid : l.append(i)
            elif i > mid : r.append(i)
            else : m.append(i)
        return quickSort(l) + m + quickSort(r)

print(quickSort([5,3,7,2,6,9,1,8,4,2,6]))
