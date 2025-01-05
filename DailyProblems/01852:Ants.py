t=int(input())
for i in range(t):
    l,n=map(int,input().split())
    ants=list(map(int,input().split()))
    ants.sort()
    maxt=max(l-ants[0],ants[-1])
    mins=set()
    for j in ants:
        mins.add(min(l-j,j))
    mint=max(mins)
    print(mint,maxt)
