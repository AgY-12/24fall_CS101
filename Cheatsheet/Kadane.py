def kadane(a):#卡丹算法求最大子序列
    max_cur=0
    max_all=0
    for i in range(len(a)):
        max_cur=max(a[i],max_cur+a[i])
        max_all=max(max_all,max_cur)
    return max_all