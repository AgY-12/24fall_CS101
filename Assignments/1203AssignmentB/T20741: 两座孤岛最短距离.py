def dfs(x,y):#找岛,返回陆地的所有坐标
    global ans
    land=[(x,y)]
    d=[(-1,0),(1,0),(0,1),(0,-1)]
    for dx,dy in d:
        nx,ny=x+dx,y+dy
        if 0<=nx<n and 0<=ny<n and mat[nx][ny]=='1':
            mat[x][y]='0'
            land+=dfs(nx,ny)
        mat[x][y]='3'
    return set(land)

n=int(input())
mat=[]
islands=[]
for _ in range(n):
    mat.append(list(input()))
for i in range(n):
    for j in range(n):
        if mat[i][j]=='1':
            islands.append(dfs(i,j))
ans=float('inf')
for i in range(len(islands)):
    for j in range(i+1,len(islands)):
        island=list(islands[i])
        another=list(islands[j])
        ans=min(abs(island[a][0]-another[b][0])+abs(island[a][1]-another[b][1])-1 for a in range(len(island)) for b in range(len(another)))
print(ans)

