import heapq

#处理输入,初始化
n=int(input())
potions=list(map(int,input().split()))
health=0
h=[]#小顶堆

#dp
for p in potions:
    heapq.heappush(h,p)
    health+=p
    if health<0:
        health-=heapq.heappop(h)

#输出
print(len(h))



