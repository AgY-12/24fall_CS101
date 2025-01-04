l,n,m=map(int,input().split())
r=[0]
distances=[]
for i in range(n):
    r.append(int(input()))
r.append(l)
for i in range(1,n+2):
    distances.append(r[i]-r[i-1])
#检查FJ期望"最小距离不低于x"能否实现
def check(x):
    num,cut=0,0
    for i in range(n+1):
        if cut+distances[i]>=x:
            num+=1
            cut=0
        else:cut+=distances[i]
    if num>=n-m+1:
        return True
    else:return False
#通过二酚查找调整FJ的期望
low,high=min(distances),sum(distances)
while high-low >0:
    mid = (low + high) // 2
    #print(low,high)
    #print('mid',mid)
    if check(mid):
        low=mid+1#如果期望能实现,就得寸进尺,调高期望
    else:
        high=mid#反之就退让,调低期望
print(low-1)
