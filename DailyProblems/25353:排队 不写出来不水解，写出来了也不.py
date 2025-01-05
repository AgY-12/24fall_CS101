n,d=map(int,input().split())
hs=[]
for i in range(n):
    hs.append(int(input()))
ans=[]
while len(ans)<n:
    #第一个非-1点，吡啶！是自由点
    i=0
    mins=[]
    maxi,mini=0,1e9+3
    if hs[i]!=-1:
        mins.append(hs[i])
        maxi=mini=hs[i]
        hs[i]=-1
    while i<len(hs)-1:
        i+=1
        if hs[i]!=-1:
            maxi,mini=max(hs[i],maxi),min(hs[i],mini)
            if maxi-hs[i]<=d and hs[i]-mini<=d:#判断自由点
                mins.append(hs[i])
                hs[i]=-1
    ans.extend(sorted(mins))
print(*ans,sep='\n')
'AC!'