cnt=0
import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)
@lru_cache(maxsize=None)
def dfs(x,y):
    global cnt
    d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    mat[x][y]='.'
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
            if mat[nx][ny]=='W':
                dfs(nx,ny)


n,m=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(input()))

for i in range(n):
    for j in range(m):
        if mat[i][j]=='W':
            dfs(i,j)
            cnt+=1
print(cnt)