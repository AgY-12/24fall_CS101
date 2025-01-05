while True:
    n,p,m=map(int,input().split())
    if (n,p,m)!=(0,0,0):

        mon=[i+1 for i in range(n)]
        j=mon.index(p)-1
        for i in range(n-1):
            j+=m
            j%=len(mon)
            print(mon.pop(j),end=',')
            j-=1
        print(mon[0])
    else:break