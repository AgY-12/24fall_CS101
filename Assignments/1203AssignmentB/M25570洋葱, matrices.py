from collections import deque
n=int(input())
onion=deque([])
for i in range(n):
    onion.append(deque(map(int,input().split())))
ans=0
while len(onion)>1:
    anstmp=sum(onion.popleft())+sum(onion.pop())+sum(onion[i].pop()+onion[i].popleft() for i in range(len(onion)))
    ans=max(ans,anstmp)
if onion:
    ans=max(ans,onion[0][0])
print(ans)