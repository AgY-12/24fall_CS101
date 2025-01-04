a,b,c=[],0,0
for i in range(5):
    a.append(list(map(int,input().split())))
    if 1 in a[i]:
        b=a[i].index(1)
        c=i
print(abs(b-2)+abs(c-2))