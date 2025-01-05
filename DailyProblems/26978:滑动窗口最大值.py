import heapq

n,k=map(int,input().split())
nums=list(map(int,input().split()))

ans=[]
window=[]
def find_max():
    global l
    while window[0][1]<l:
        heapq.heappop(window)
    return (-1)*window[0][0]

for i in range(k):
    heapq.heappush(window,((-1)*nums[i],i))
ans.append((-1)*window[0][0])

for r in range(k,len(nums)):
    l=r-k+1#l,r从1,k开始
    heapq.heappush(window,((-1)*nums[r],r))
    ans.append(find_max())

print(*ans)








