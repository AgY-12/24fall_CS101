n=int(input())
king=tuple(map(int,input().split()))
officials=[]
for i in range(n):
    officials.append(tuple(map(int,input().split())))
officials.sort(key=lambda x:x[0]*x[1])
pi=[king[0]]
for i in range(n):
    pi.append(officials[i][0]*pi[-1])
ans=king[0]//officials[0][1]
for i in range(1,n):
    ans=max(ans,pi[i]//officials[i][1])
print(ans)