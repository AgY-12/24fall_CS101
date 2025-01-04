#pylint:skip-file
from collections import deque
def bfs(x1,y1,x2,y2,end):
    global mat
    q=deque([(x1,y1,x2,y2)])
    d=[(0,1),(0,-1),(-1,0),(1,0)]
    visited=set()
    while q:
        x1,y1,x2,y2=q.popleft()
        for dx,dy in d:
            visited.add((x1,y1,x2,y2))
            if end in [(x1,y1),(x2,y2)]:
                return 'yes'
            nx1,ny1,nx2,ny2=x1+dx,y1+dy,x2+dx,y2+dy
            if 0<=nx1<len(mat) and 0<=nx2<len(mat) \
                and 0<=ny1<len(mat[0]) and 0<=ny2<len(mat[0]):
                    if (nx1,ny1,nx2,ny2) not in visited \
                        and 1 not in (mat[nx1][ny1],mat[nx2][ny2]):
                            q.append((nx1,ny1,nx2,ny2))
    return 'no'

n=int(input())
mat=[]
start=[]
end=()
for i in range(n):
    mat.append(list(map(int,input().split())))
    while 5 in mat[i]:
        start+=[i,mat[i].index(5)]
        mat[i][mat[i].index(5)]=0
    if 9 in mat[i]:
        end=(i,mat[i].index(9))
print(bfs(start[0],start[1],start[2],start[3],end))