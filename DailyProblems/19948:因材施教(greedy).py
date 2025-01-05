n,m=map(int,input().split())
m-=1
stu=list(map(int,input().split()))
stu.sort()
delta=[]
for i in range(n-1):
    delta.append(stu[i+1]-stu[i])
delta.sort()
for i in range(m):
    delta.pop()
print(sum(delta))