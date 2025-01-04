l=list(map(int,input().split(',')))
n=len(l)
def solve():
    k=max( l )
    if k<0:
        return k
    la1=[-float('inf')]*n
    la2=la1[:]
    la1[0]=l[0]
    la2[-1]=l[-1]
    for i in range(1,n):
        la1[i]=max(la1[i-1]+l[i],l[i])
        la2[n-i-1]=max(la2[n-i]+l[n-i-1],l[n-i-1])
    ans=max(la1)
    for i in range(1,n-1):
        ans=max(ans,la1[i-1]+la2[i+1])
    return ans
print(solve())