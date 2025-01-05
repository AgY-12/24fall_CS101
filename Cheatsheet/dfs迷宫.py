def dfs(x, y, e, S=0):
    d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    ans = []
    if (x, y) == e:
        return S
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
            if mat[nx][ny] == 1:
                mat[x][y] = 0
                ans.append(dfs(nx, ny, e, S + 1))
                mat[x][y] = 1
    return (min(ans))
n,m=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
while True