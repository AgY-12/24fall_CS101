n=int(input())
dp=[0]*(n+1)
dp[1]=1
for i in range(1,n+1):
    dp[i]=sum(dp[j] for j in range(i))+1
print(dp[n])