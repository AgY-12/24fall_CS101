import sys
input=sys.stdin.readlines()
mat=[]
for line in input:
    mat.append(list(map(int,line.split())))
sol=[[0]*len(mat[0]) for _ in range(len(mat))]
def click(x,y):
    sol[x][y]=int(not sol[x][y])
    mat[x][y]=int(not mat[x][y])
    d=[(1,0),(-1,0),(0,1),(0,-1)]
    for dx,dy in d:
        if 0<=x+dx<len(mat) and 0<=y+dy<len(mat[0]):
            mat[x+dx][y+dy]=int(not mat[x+dx][y+dy])
while True:
    '''
    for _ in sol:
        print(*_)
    print('__________')
    '''
    for i in range(0,len(mat)-1):
        for j in range(0,len(mat[0])):
            if mat[i][j]==1:
                click(i+1,j)

    if 1 not in mat[-1]:break
    for i in range(len(mat)-1,0,-1):
        for j in range(0,len(mat[0])):
            if mat[i][j]==1:
                click(i-1,j)
    if 1 not in mat[0]:break

    for i in range(0,len(mat[0])-1):
        for j in range(0,len(mat)):
            if mat[j][i]==1:
                click(j,i+1)
    if sum(mat[i][-1] for i in range(len(mat)))==0:break
    for i in range(len(mat[0])-1,0,-1):
        for j in range(0,len(mat)):
            if mat[j][i]==1:
                click(j,i-1)
    if sum(mat[i][0] for i in range(len(mat)))==0:break

for _ in sol:
    print(*_)