n,m=map(int,input().split())
tv=list(map(int,input().split()))
tv.sort()
i=0
money=0
while i<=len(tv)-1 and tv[i]<0 and m>0  :
    money-=tv[i]
    m-=1
    i+=1
print(money)