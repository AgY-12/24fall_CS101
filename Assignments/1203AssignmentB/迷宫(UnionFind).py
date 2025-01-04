def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])#把所有家长节点都指向根节点
    return parent[x]#返回根节点
def union(x,y):
    parent[find(x)]=find(y)#把x的根连到y的根上
n,m=map(int,input().split())
parent=list(range(n+1))
for i in range(m):
    a,b=map(int,input().split())
    union(a,b)
f=find(1)
for i in range(1,n+1):
    if f==find(i):
        continue
    else:
        print('No')
        break
else:print('Yes')