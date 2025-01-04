def compare(a,b):
    if int(a+b)>int(b+a):return '>'
    elif int(a+b)==int(b+a): return '='
    else:return '<'
def Mergesort(alist):
    if len(alist)<=1:
        return alist
    left=Mergesort(alist[:len(alist)//2])
    right=Mergesort(alist[len(alist)//2:])
    return Merge(left,right)
def Merge(left,right):
    ru=[]
    l,r=0,0
    while l<len(left) and r<len(right):
        if compare(left[l],right[r])!='>':
            ru.append(left[l])
            l+=1
        else:
            ru.append(right[r])
            r+=1
    ru+=left[l:]+right[r:]
    return ru
n=int(input())
nums=list(input().split())
numsorted=Mergesort(nums)
print(*numsorted[::-1],sep='',end=' ')
print(*numsorted,sep='')
'''
过——————————了——————————————！！！！！！！！
'''

