l,m=map(int,input().split())
list=list(range(l))
list.append(l)
#print(list)
for i in range(m):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        list[j]='*'
print(l+1-list.count('*'))