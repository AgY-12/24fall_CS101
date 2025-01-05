import bisect
def lis(a):
    dp=[float('inf')]*(len(a)+2)
    for i in range(len(a)):
        dp[bisect.bisect_left(dp,a[i])]=a[i]
    print(dp)
    return bisect.bisect_left(dp,float('inf'))
a=[5,3,7,2,3,3,6,1,8]
print(lis(a))