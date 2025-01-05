n,w=map(int,input().split())
itms=[]
for _ in range(n):
    itms.append(list(map(int,input().split())))
itms.sort(key=lambda x:x[1]/x[0],reverse=True)
ans=0
for i in itms:
    if w>=i[0]:
        ans+=i[1]
        w-=i[0]
    else:
        continue
print(ans)

'''
这种做法不行，比如说：
n=3,w=3
3 5
1 1
1 1
1 2
如果遵循性价比原则，拿了1 2，那就只剩两个1 1可以拿，总价值为4；
如果一次性拿3 5，总价值为5。
所以“性价比原则”不适用与01背包。
'''