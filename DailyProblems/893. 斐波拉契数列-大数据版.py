n=int(input())
MAXN=int(1e9+7)
fbnc=[1,1,2]
cnt=2
while fbnc[1::]!=[1,1]:
    fbnc.append(fbnc[-1]+fbnc[-2])
    fbnc[0],fbnc[1]=fbnc[1],fbnc[2]%MAXN
    cnt+=1
print(cnt)