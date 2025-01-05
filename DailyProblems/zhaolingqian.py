'''
5种硬币：1，,5，,10，,21，,25，怎么找到最少数量的硬币，来达到特定数量的钱？
'''
n=int(input())
dp=[0]*1000
track=[[] for _ in range(1000)]
for i in range(1,n+1):
    tmp=list(set(range(i+1)).intersection({1,5,10,21,25}))
    besti=1

    for j in tmp:
        if dp[i-j]<dp[i-besti]:
            besti=j
    dp[i]=min(dp[i-k]+1 for k in tmp)
    track[i]=track[i-besti]+[besti]
print(dp[n])
print(track[n])