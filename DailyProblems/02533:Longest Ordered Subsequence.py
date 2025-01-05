n=int(input())
arr=list(map(int,input().split()))
dp=[0]*len(arr)
maxl=1
for k in range(len(arr)):
    #print(dp)
    if k==0:dp[k]=1
    else:
        t=False
        for j in range(k):
            if arr[j]<arr[k]:
                dp[k]=max(dp[k],dp[j]+1)
                t=True
        if not t:dp[k]=1
        maxl=max(maxl,dp[k])
print(maxl)