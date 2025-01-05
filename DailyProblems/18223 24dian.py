n=input()
n=int(n)
for i in range(n):
    ru = []
    a,b,c,d=map(int,input().split())
    for j in range(1,-2,-2):
        u=a*j
        for k in range(1,-2,-2):
            v=b*k
            for l in range(1,-2,-2):
                w=c*l
                for m in range(1,-2,-2):
                    x=d*m
                    ru.append(u+v+w+x)
    if 24 in ru:
        print('YES')
    else:
        print('NO')

