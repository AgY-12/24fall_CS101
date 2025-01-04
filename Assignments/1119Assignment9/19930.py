from collections import deque


def bfs(x,y):
    q=deque([(x,y,0)])
    d=[(-1,0),(0,1),(0,-1),(1,0)]
    while q:
        x,y,cnt=q.popleft()
        if mat[x][y]==1:
            return cnt
        mat[x][y]=2
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
                if mat[nx][ny]==0:
                    q.append((nx,ny,cnt+1))
                elif mat[nx][ny]==1:
                    return cnt+1
    else:return('NO')
n,m=map(int,input().split())
mat=[]
for _ in range(n):
    mat.append(list(map(int,input().split())))
print(bfs(0,0))