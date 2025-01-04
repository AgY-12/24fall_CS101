#pylint:skip-file
def dfs(x,y,cnt):
    global n,m,path,mat
    d=[(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]
    if cnt==n*m:
        path+=1
        return
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<m and mat[nx][ny]==0:

            mat[x][y]=1
            dfs(nx,ny,cnt+1)
            mat[x][y]=0
t=int(input())
for i in range(t):
    n,m,x,y=map(int,input().split())
    path=0
    mat=[[0]*m for _ in range(n)]
    dfs(x,y,1)
    print(path)