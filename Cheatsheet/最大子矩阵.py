def qzh(mat,n,m):
    qzh=[]
    for i in range(n):
        qzh.append([0])
        for j in range(m):qzh[i].append(qzh[i][-1]+mat[i][j])
    return qzh
def kadane(a):#卡丹算法求最大子序列
    max_cur=0
    max_all=0
    for i in range(len(a)):
        max_cur=max(a[i],max_cur+a[i])
        max_all=max(max_all,max_cur)
    return max_all
def max_submat(qzh,n,m):

    #现在我要算每个对于左边界为l，右边界为r的，上下浮动和伸缩的一系列子矩阵的最大值
    maxn=0
    for l in range(1,m+1):
        for r in range(l,m):
            a=list(qzh[i][r]-qzh[i][l-1] for i in range(n))
            maxn=max(maxn,kadane(a))
    return(maxn)
#主函数
n,m=map(int,input().split())#列数:m,行数:n
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
qzh=qzh(mat,n,m)
print(max_submat(qzh,n,m))