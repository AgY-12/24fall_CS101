t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    sa=sb=0
    ma=mb=1e9+9
    for i in range(n):
        sa+=a[i]
        ma=min(a[i],ma)
        sb+=b[i]
        mb=min(b[i],mb)
    #print('ma',ma,'mb',mb,'sa',sa,'sb',sb)
    s=min(sa+n*mb,n*ma+sb)
    print(s)