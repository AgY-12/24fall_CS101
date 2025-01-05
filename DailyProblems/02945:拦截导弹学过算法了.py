k=int(input())
h=list(map(int,input().split()))+[-1]
h.reverse()
h.append(1e15)
#print(h)
mat=[-1]+[[0 for i in range(k-j)] for j in range(k)]
for _ in range(k+1,1,-1):
    mat[1][k+1-_]=int(h[_]>=h[1])
for i in range(2,k+1):#行，h[i]是现在需要打不打的那个的高度
    for j in range(k+1,i,-1):#列，h[j]是最大能打高度.
        if h[j]>=h[i]:
            mat[i][k+1-j]=max(1+mat[i-1][k+1-(i)],mat[i-1][k+1-j])
        else:
            mat[i][k+1-j]=mat[i-1][k+1-j]
print(mat[-1][-1])
'''
状态转移方程：
f(i,j)=
    1+f(i-1,i),打
    f(i-1,j),不打
'''

