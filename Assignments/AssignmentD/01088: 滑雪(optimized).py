import heapq

mat=[]
h=[]
r,c=map(int,input().split())
for i in range(r):
    mat.append(list(map(int,input().split())))
    for j in range(c):
        heapq.heappush(h,(mat[i][j],i,j))
dp=[[1]*c for _ in range(r)]
d=[(-1,0),(0,1),(1,0),(0,-1)]
ans=1
while h:
    height,x,y=heapq.heappop(h)
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<r and 0<=ny<c and mat[nx][ny]<height and dp[nx][ny]+1>dp[x][y]:
            dp[x][y]=dp[nx][ny]+1
            ans=max(ans,dp[x][y])
print(ans)