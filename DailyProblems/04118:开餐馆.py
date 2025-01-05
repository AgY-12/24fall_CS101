from collections import defaultdict
import bisect
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    m=list(map(int,input().split()))
    p=list(map(int,input().split()))
    dp=defaultdict(list)
    #dp[position][0]是position位置不开，前面确定，后面不管，截止position位置的最大利润
    dp[m[0]]=[0,p[0]]
    for i in range(1,len(m)):
        position=m[i]
        last_position=m[i-1]
        #print('position:',position)
        mlp_index=bisect.bisect_left(m, position - k) - 1
        max_legal_position=m[mlp_index]
        #print('mlp:',max_legal_position)
        #print(dp[max_legal_position])
        dp[position].append(max(dp[last_position][0],dp[last_position][1]))
        if mlp_index>=0:
            dp[position].append(max(dp[max_legal_position][0],dp[max_legal_position][1])+p[i])
        else:dp[position].append(p[i])
    print(max(dp[m[-1]][0],dp[m[-1]][1]))


