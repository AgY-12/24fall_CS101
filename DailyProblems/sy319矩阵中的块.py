from collections import deque
cnt=0
def bfs(mat,x0,y0):
    global cnt
    d=[(-1,0),(1,0),(0,-1),(0,1)]
    q=deque([(x0,y0)])
    visited=set()
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
                if mat[nx][ny]==1:
                    q.append((nx,ny))
                    visited.add((nx,ny))
        mat[x][y]=0
    cnt+=1
n,m=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if mat[i][j]==1:
            bfs(mat,i,j)
print(cnt)