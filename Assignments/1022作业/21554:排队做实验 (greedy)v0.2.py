n=int(input())
stu=list(map(int,input().split()))
for i in range(n):
    stu[i]=[stu[i],i+1]
stu.sort(key=lambda x:x[0])
print(*(list(stu[i][1] for i in range(n))),sep=' ')
sum=0
for i in range(1,n+1):
    sum+=stu[i-1][0]*(n-i)
print("{:.2f}".format(sum/n))
