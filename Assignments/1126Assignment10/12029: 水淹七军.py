from collections import deque
import sys
MAXN=1111
def bfs(x,y):
    global slb,mat
    q=deque([(x,y)])
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    dead=[[0]*(n+1) for _ in range(m+1)]
    drowned=[[0]*(n+1) for _ in range(m+1)]
    while q:
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 1<=nx<=m and 1<=ny<=n \
            and mat[nx][ny]<=mat[x][y] :
                if (nx,ny)==slb:
                    return('Yes')
                if mat[nx][ny]<mat[x][y] or dead[nx][ny]==0:
                    q.append((nx,ny))
                    mat[nx][ny]=mat[x][y]
                    drowned[nx][ny]=1
                    dead[nx][ny]=0
        dead[x][y]=1


    return ('No')
lines=list(sys.stdin.read().split())

t=int(lines[0])
id=1
for _ in range(t):
    m,n=map(int,(lines[id],lines[id+1]))
    mat=[[MAXN]*(n+2)]
    id+=2
    for i in range(m):
        mat.append([MAXN]+list(map(int,lines[id:id+n]))+[MAXN])
        id+=n
    mat.append([MAXN]*(n+2))
    slb=(int(lines[id]),int(lines[id+1]))
    id+=2
    k=int(lines[id])
    id+=1
    H2O=[]
    for i in range(k):
        H2O.append((int(lines[id]),int(lines[id+1])))
        id+=2
    for h20 in H2O:
        ans=bfs(h20[0],h20[1])
        if ans=='Yes':
            print(ans)
            break
    else:print('No')