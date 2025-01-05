while True:
    try:
        n=int(input())
        t=n
        dp=[[0]*52 for i in range(52)]
        for i in range(1,n+1):
            dp[i][i]=1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                #print(f'dp[{i}][{j}]={dp[i][j]}')
                dp[i][j]=sum(dp[i-j][k] for k in range(j,(i-j)//2+1))+1
                #print(f'-->dp[{i}][{j}]={dp[i][j]}')
        print(sum(dp[n]))
    except EOFError:break

