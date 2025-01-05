import heapq
from collections import defaultdict
n=int(input())
s=[]
s_bucket=defaultdict(int)
e=[]
e_bucket=defaultdict(int)
def love():
    while s and s_bucket[-1*s[0]]<=0:
        heapq.heappop(s)
    while e and e_bucket[e[0]]<=0:
        heapq.heappop(e)
    if s and -1*s[0]>e[0]:
        return 'YES'
    else: return 'NO'
for _ in range(n):
    line=input().split()
    if line[0]=='+':
        heapq.heappush(s,(int(line[1])*(-1)))#s做成大根堆
        s_bucket[int(line[1])]+=1
        heapq.heappush(e,(int(line[2])))#e做成小根堆,如果max(|s|)>min(e),就YES
        e_bucket[int(line[2])]+=1
    elif line[0]=='-':
        s_bucket[int(line[1])]-=1
        e_bucket[int(line[2])]-=1

    print(love())
'''
Can I fall in love if I've solved the problem? wwww
'''
