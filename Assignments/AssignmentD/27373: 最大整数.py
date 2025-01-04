m=int(input())
n=int(input())
arr=list(map(int,input().split()))
arr.sort(key=lambda x:x/(10**len(str(x))-1),reverse=True)
dp=['']*(205)
ans=0
for i in arr:
    tmp={len(str(i)):str(i)}
    for j in dp:
        if len(str(j)+str(i))<=m:
            tmp[len(j+str(i))]=str(j)+str(i)
    for k,v in tmp.items():
        dp[k]=str(max(dp[k],str(v)))
        ans=max(ans,int(dp[k]))
print(ans)
'''
5
5
999 8 433 322 1111
'''
