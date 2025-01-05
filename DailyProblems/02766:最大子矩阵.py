n=int(input())
matlist=[]
mat=[]
try:
    while True:
        line=list(map(int,input().split()))
        #print(line)
        if line==[9999]:raise EOFError
        matlist+=line
except EOFError:
    for i in range(0,n**2,n):
        mat.append(matlist[i:i+n])
    dp=[[[0,1,1]]*(n+1) for _ in range(n+1)]#zhe ge dp chule jilu meige zhongjieweizhi d zuida juzhen daxiao,
    # haiyao jilu nage zuida juzhen d changyukuan
    maxn=0
    for row in range(1,n+1):
        for col in range(1,n+1):#注意mat里面用的是0-n，dp加了保护层是1-（n+1）
            for _ in range(len(dp)):print(dp[_])
            print('')
            tmp=[]
            for _ in range(len(mat)): print(mat[_])
            up=dp[row-1][col][0]+sum(list(mat[row-1][col-i-1] for i in range(dp[row-1][col][1])))
            left=dp[row][col-1][0]+sum(list(mat[row-i-1][col-1] for i in range(dp[row][col-1][2])))
            tmp.append([up,dp[row-1][col][1],dp[row-1][col][2]+1])
            tmp.append([left,dp[row][col-1][1]+1,dp[row][col-1][2]])
            tmp.sort(key=lambda x:x[0])
            print(tmp)
            dp[row][col]=tmp[-1]
            if row==1:dp[row][col][2]=1
            if col==1:dp[row][col][1]=1
            maxn=max(maxn,dp[row][col][0])
    print(maxn)