def dp(n,b,v,w):
    dp=[[0]*(b+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,b+1):
            if j>=w[i-1]:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i-1]]+v[i-1])
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][b]



n,b=map(int,input().split())
v=list(map(int,input().split()))
w=list(map(int,input().split()))
print(dp(n,b,v,w))