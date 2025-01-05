n,m=map(int,input().split())
mat=[[0 for _ in range(m+2)]]
for i in range(n):
    mat.append([0]+list(map(int,input().split()))+[0])
mat.append([0 for _ in range(m+2)])
newmat=[[0 for _ in range(m)] for __ in range(n)]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
for i in range(1,n+1):
    for j in range(1,m+1):
        s=0
        #for k in range(8):
            #s+=mat[i+dx[k]][j+dy[k]]
        s=mat[i-1][j-1]+mat[i-1][j]+mat[i-1][j+1]+mat[i][j-1]+mat[i][j+1]+mat[i+1][j-1]+mat[i+1][j]+mat[i+1][j]+mat[i+1][j+1]
        if s==2 :
            newmat[i-1][j-1]=mat[i][j] and 1
        elif s==3:
            newmat[i-1][j-1]=1
        else:newmat[i-1][j-1]=0
for i in newmat:
    print(*i)