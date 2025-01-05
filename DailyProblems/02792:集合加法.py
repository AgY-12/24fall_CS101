t=int(input())
for _ in range(t):
    s = int(input())
    ans = 0
    p={i:0 for i in range(1,10001)}
    q={i:0 for i in range(0,10001)}
    lp = int(input())
    p_t = (map(int, input().split()))
    lq = int(input())
    q_t = (map(int, input().split()))
    for i in p_t:
        p[i]+=1
    for j in q_t:
        q[j]+=1
    for i in range(1,10001):
        ans+=p[i]*q[max((s-i),0)]
    print(ans)
    '''
    s=int(input())
    ans=0
    lp=int(input())
    p=list(map(int,input().split()))
    lq=int(input())
    q=list(map(int,input().split()))
    for j in p:
        ans+=q.count(s-j)
    print(ans)
    '''
    '''
    2
99
2
49 49
2
50 50
11
9
1 2 3 4 5 6 7 8 9
10
10 9 8 7 6 5 4 3 2 1

'''