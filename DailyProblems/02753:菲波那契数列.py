n=int(input())
a=[1,1]
for i in range(19):
    a.append(a[-1]+a[-2])
for i in range(1,n+1):
    print(a[int(input())-1])