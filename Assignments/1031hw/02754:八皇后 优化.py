ans=[]
def queen(A, cur=0):
    if cur == len(A):
        ans.append(A[:])
        return 0
    for col in range(1,len(A)+1):  # 遍历当前行的所有位置
        A[cur] = col
        for row in range(cur):  # 检查当前位置是否相克
            if A[row] == col or abs(col - A[row]) == cur - row:
                break
        else:  # 如果完成了整个遍历，则说明位置没有相克
            queen(A, cur+1)  # 计算下一行的位置
queen([None]*8)
t=int(input())
for i in range(t):
    n=int(input())
    print(*ans[n-1],sep='')