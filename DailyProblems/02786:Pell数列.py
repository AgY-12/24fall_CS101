a=[1,2]
for i in range(148):
    a.append((a[-1]*2+a[-2])%32767)
n=int(input())
for i in range(n):
    k=int(input())
    k%=150
    print(a[k-1])
