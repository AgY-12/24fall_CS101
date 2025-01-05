def dp(b,w):
    dp=[0]*4001
    for j in range(min(w),b+1):
        if j>=min(w):
            tmp=[0,0,0]
            for i in range(3):
                if (j-w[i]>=min(w) or j-w[i]==0) and dp[j-w[i]]!=-1:
                    tmp[i]=dp[j-w[i]]+1
                else:
                    tmp[i]=-1
            dp[j]=max(tmp)

    return dp[b]
N,A,B,C=map(int,input().split())
print(dp(N,[A,B,C]))
'''
类似于完全背包
'''