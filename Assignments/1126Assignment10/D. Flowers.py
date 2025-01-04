import sys
MAXN=1000000007
def dp(maxin):
    dp = [1] * (100099)
    ans = list(range(k))+[k+1]  # 存前缀和的，到时候输出就直接ans[b]-ans[a-1]
    anstmp = ans[-1]
    dp[k]=2
    for n in range(k+1,maxin+1):
        dp[n]=(2*dp[n-k]+ans[n-k-1]-ans[n-2*k])%MAXN if (n-2*k) >=0 else (2*dp[n-k]+ans[n-k-1]+1)%MAXN
        anstmp+=dp[n]
        anstmp%=MAXN
        ans.append(anstmp%MAXN)
    return ans
pyin=sys.stdin.readlines()
t,k=map(int,pyin[0].split())
maxin=0
pyin.pop(0)
for line in pyin:
    a,b=map(int,line.split())
    maxin=max(a,b,maxin)
ans=dp(maxin)
for line in pyin:
    a,b=map(int,line.split())
    print((ans[b]-ans[a-1])%MAXN)