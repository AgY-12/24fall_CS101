#熄灯问题数据生成.生成两个矩阵,第一个是题,第二个是解
import random

mat=[[0]*6 for _ in range(5)]
sol=[[0]*6 for _ in range(5)]
def click(x,y):
    sol[x][y]=int(not sol[x][y])
    mat[x][y]=int(not mat[x][y])
    d=[(1,0),(-1,0),(0,1),(0,-1)]
    for dx,dy in d:
        if 0<=x+dx<len(mat) and 0<=y+dy<len(mat[0]):
            mat[x+dx][y+dy]=int(not mat[x+dx][y+dy])
for i in range(random.randint(90,100)):
    x=random.randint(0,4)
    y=random.randint(0,5)
    click(x,y)
for _ in mat:
    print(*_)
print('-------')
for _ in sol:
    print(*_)