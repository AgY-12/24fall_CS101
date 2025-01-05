import bisect

t=int(input())
for _ in range(t):
    dplist=[1]*5005
    n=int(input())
    b=list(map(int,input().split()))
    a=[]
    for i in range(0,len(b),2):
        a.append((b[i],b[i+1]))
    a.sort(key=lambda x: (x[0],x[1]),reverse=True)
    #print(a)
    stk=[]
    f=[a[i][1] for i in range(len(a))]
    for k in range(n):
        #print(stk)
        t=bisect.bisect_left(stk,f[k])
        if t < len(stk) :
            stk[t]=f[k]
        else:
            stk.append(f[k])
    print(len(stk))