N=int(input())
ans=0
for K in range(1,N+1):
    dp = [[0] * (K + 1) for i in range(N + 1)]
    for i in range(0, N + 1):  # 将i分成1个数只有一种方案
        dp[i][1] = 1

    for i in range(1, N + 1):
        for j in range(2, K + 1):
            if j <= i:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
    ans+=dp[N][K]
print(ans)