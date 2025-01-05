from collections import deque


def bfs(mat):
    ans=[[-1]*len(mat[0]) for _ in range(len(mat))]
    d=[(-1,0),(0,1),(1,0),(0,-1)]
    q=deque([(0,0,0)])#q[0],q[1]分别是点的x和y，q[2]（也即后面的i）是走几步

    while q:
        '''
        for _ in mat:
            print(*_, sep=' ')
        
        print(x,y,i,'\n')
        '''
        x,y,i=q.popleft()
        for dx,dy in d:
            #print(q)
            nx,ny=x+dx,y+dy
            if 0<=nx<len(mat) and 0<=ny<len(mat[0]):
                if mat[nx][ny]==0:
                    q.append((nx,ny,i+1))
                    ans[nx][ny]=i+1
                    mat[nx][ny]=2
        mat[x][y]=2
    ans[0][0]=0
    return ans

n,m=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
answer=bfs(mat)
for _ in answer:
    print(*_,sep=' ')




