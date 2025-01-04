path=[]
max_path=[]
w=0
wmax=-999999
def dfs(x,y):
    global n,m,w,wmax,max_path
    w+=mat[x][y]
    path.append((x,y))
    d=[(1,0),(0,1),(-1,0),(0,-1)]
    if (x,y)==(n,m):
        #print(f'终点\npath={path},\nw={w}')
        if w>wmax:
            wmax=w
            max_path=path[:]
        path.pop(-1)
        w-=mat[x][y]
        return
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 1<=nx<=n and 1<=ny<=m and not visited[nx][ny]:
            visited[x][y]=1
            dfs(nx,ny)
            visited[x][y]=0
    path.pop(-1)
    w-=mat[x][y]
n,m=map(int,input().split())
mat=[[0]*(1+m)]
for i in range(n):
    mat.append([0]+list(map(int,input().split())))
visited=[[0]*(1+m) for _ in range(n+1)]
dfs(1,1)
for i in max_path:
    print(*i,sep=' ')
