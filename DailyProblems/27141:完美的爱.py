from collections import defaultdict
n=int(input())
gift=list(map(int,input().split()))
gift[0]-=520#全减520,归零!前缀和中哪两个地方有数相等,这两个地方之间平均值就是520
qzh=[gift[0]]
bucket=defaultdict(list)#存储前缀和中每个数的位置
bucket[0].append(-1)
bucket[gift[0]].append(0)
for i in range(1,len(gift)):
    gift[i]-=520
    qzh.append(gift[i]+qzh[i-1])
    if len(bucket[qzh[-1]])<2:#桶里存储qzh中每个数出现的最小位置和最大位置
        bucket[qzh[-1]].append(i)
    else:
        bucket[qzh[-1]][-1]=i
ans=0
for i in bucket.values():
    if len(i)>1:
        ans=max(ans,(i[1]-i[0])*520)
print(ans)
print(qzh)
print(bucket)