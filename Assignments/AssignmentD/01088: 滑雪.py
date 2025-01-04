from functools import lru_cache

mat=[]
@lru_cache(maxsize=None)
def dfs(x,y):
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    l_tmp=1
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
            if mat[nx][ny]<mat[x][y]:
                l_tmp=max(l_tmp,dp[nx][ny]+1) if dp[nx][ny]!=0 else max(l_tmp,dfs(nx,ny)+1)
    return l_tmp

r,c=map(int,input().split())
for i in range(r):
    mat.append(list(map(int,input().split())))
dp=[[0]*c for _ in range(r)]
ans=1
for i in range(r):
    for j in range(c):
        if dp[i][j]==0:
            dp[i][j]=dfs(i,j)
        ans=max(ans,dp[i][j])
print(ans)