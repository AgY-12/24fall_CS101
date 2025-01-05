m,n,p,q=map(int,input().split())
lmat=[]
smat=[]
for i in range(m):
    lmat.append(list(map(int,input().split())))
for i in range(p):
    smat.append(list(map(int,input().split())))
ansmat=[[] for _ in range(m+1-p)]
for i in range(m+1-p):
    for j in range(n+1-q):
        t=0
        for k in range(p):
            for l in range(q):
                t+=smat[k][l]*lmat[i+k][j+l]
        ansmat[i].append(t)
for i in ansmat:
    for j in i:
        print(j,end=" ")
    print('')