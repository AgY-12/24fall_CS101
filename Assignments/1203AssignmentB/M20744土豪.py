v=list(map(int,input().split(',')))
n=len(v)
dp1=[-float('inf')]*n
dp2=dp1[:]
dp1[0]=v[0]
dp2[-1]=v[-1]
for i in range(1,n):
    dp1[i]=max(dp1[i-1]+v[i],v[i])
    dp2[n-i-1]=max(dp2[n-i]+v[n-i-1],v[n-i-1])
ans=max(dp1)
for i in range(1,n-1):
    ans=max(ans,dp1[i-1]+dp2[i+1])
print(ans)