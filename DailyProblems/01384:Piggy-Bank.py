def dpbank(coins,e,f):
    dp = [0] + [1e9] * (f - e + 8)
    for i in range(1, f - e + 1):
        for j in coins:

            if j[1] > i:
                continue
            elif dp[i - j[1]] == -1:
                continue
            else:
                if dp[i - j[1]] + j[0] < dp[i]:
                    dp[i] = dp[i - j[1]] + j[0]
                    continue
        if dp[i] == 1e9: dp[i] = -1
    if dp[f - e] != -1:
        print(f'The minimum amount of money in the piggy-bank is {dp[f - e]}.')
    else:
        print('This is impossible.')

t=int(input())
for T in range(t):
    e,f=map(int,input().split())
    coins=[]
    n=int(input())
    for i in range(1,n+1):
        v,w=map(int,input().split())
        coins.append((v,w))
    coins.sort(key=lambda x:(x[1],x[0]))
    dpbank(coins,e,f)
    #print(dp)
