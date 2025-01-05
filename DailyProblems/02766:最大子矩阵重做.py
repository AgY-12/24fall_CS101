
matlist=[]
mat=[]
import sys
inp=sys.stdin.readlines()
n=int(inp[0])
for line in inp[1::]:
    line=map(int,line.strip().split())
    matlist+=list(line)
for i in range(0,n**2,n):
    mat.append(matlist[i:i+n])
'''
n=int(input())
matlist=[]
mat=[]
try:
    while True:
        line=list(map(int,input().split()))
        #print(line)
        if line==[9999]:raise EOFError
        matlist+=line
except EOFError:
    for i in range(0,n**2,n):
        mat.append(matlist[i:i+n])
    dp=[[[0,1,1]]*(n+1) for _ in range(n+1)]
'''
#建立前缀和矩阵
qzh=[]
for i in range(n):
    qzh.append([0])
    for j in range(n):qzh[i].append(qzh[i][-1]+mat[i][j])

def kadane(a):#卡丹算法求最大子序列
    max_cur=0
    max_all=0
    for i in range(len(a)):
        max_cur=max(a[i],max_cur+a[i])
        max_all=max(max_all,max_cur)
    return max_all
#现在我要算每个对于左边界为l，右边界为r的，上下浮动和伸缩的一系列子矩阵的最大值
maxn=0
for l in range(1,n+1):
    for r in range(l,n):
        a=list(qzh[i][r]-qzh[i][l-1] for i in range(n))
        maxn=max(maxn,kadane(a))
print(maxn)

#Accepted!