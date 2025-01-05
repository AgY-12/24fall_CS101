n=int(input())
t=n
dp=[[0]*52 for i in range(52)]
for i in range(0,n+1):
    dp[i][1]=dp[i][i]=1
for i in range(2,n+1):
    for j in range(2,i):
        for k in range(i%j,i-j+1,j):
            dp[i][j]+=sum(dp[k][l] for l in range(1,j))

print(sum(dp[n]))
for _ in dp[:n+2]:
    print(*_,sep=' ')