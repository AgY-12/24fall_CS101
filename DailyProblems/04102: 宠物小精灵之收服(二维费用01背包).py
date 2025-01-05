n,m,k=map(int,input().split())
pkms=[]
for _ in range(k):
    pkms.append(list(map(int,input().split())))

dp=[[0]*(m+2) for _ in range(n+2)]
maxhealth=m
for pkm in pkms:
    for ball in range(n,pkm[0]-1,-1):
        for health in range(m,pkm[1]-1,-1):

            if dp[ball-pkm[0]][health-pkm[1]]+1>dp[ball][health]:
                dp[ball][health]=dp[ball-pkm[0]][health-pkm[1]]+1
                if ball==n and health==m:
                    maxhealth-=pkm[1]


print(dp[n][m],maxhealth)
