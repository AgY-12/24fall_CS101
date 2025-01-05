n=int(input())
arr=list(map(int,input().split()))
'''
2 6 3
4 5 1

2
6 3
4 
5 1

2 3 6(+1)
1 4 5(+1)(+1)


1 2 3 4 5 6(+3)(+1)(+1)
每次归并排的时候，放进去一个left元素，它前面有多少个right里面的元素，就答案加几，

'''
ans=0
def mergesort(arr):
    if len(arr)==1:return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    global ans
    l,r=0,0
    merged=[]

    while l<len(left) and r<len(right):
        #print('pai:',left, right, left[l], right[r])
        #print('merged:',merged,'ans:',ans)
        if left[l]<right[r]:
            merged.append(left[l])
            l+=1
            ans+=r
        elif left[l]>right[r]:
            merged.append(right[r])
            r+=1
        #print('updated!merged:',merged)
        #print('updated!ans:',ans)
    merged.extend(left[l:])
    merged.extend(right[r:])
    ans+=len(left[l:])*len(right)
    return merged
mergesort(arr)
print(ans)
