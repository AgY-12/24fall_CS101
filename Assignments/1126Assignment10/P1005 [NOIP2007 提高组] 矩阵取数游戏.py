n,m=map(int,input().split())
from collections import deque
mat=[]
for i in range(n):
    mat.append(deque(map(int,input().split())))
ans=0
for i in range(1,m+1):
    for j in range(n):
        if mat[j][0]<mat[j][-1]:
            ans+=mat[j].popleft()*(2**i)
        else:ans+=mat[j].pop()*(2**i)
print(ans)