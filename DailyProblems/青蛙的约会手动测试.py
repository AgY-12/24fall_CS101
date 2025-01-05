def date(x,y,m,n,L):
    k=0
    while (x+k*m)%L!=(y+k*n)%L :
        k+=1
    return k
'''
a=[]
b=[]
for x in range(7,10):
    print('x=',x)
    for y in range(7,10):
        print('y=',y)
        if y!=x:
            for m in range(1,10):
                print('m=',m)
                for n in range(1,10):
                    for L in range(max(x,y)+1,20):
                        b.append([x,y,m,n,L])
                        a.append(date(x,y,m,n,L))
for i in b:
    for j in i:
        print(j,end=' ')
    print('')
for i in a:
    print(i)


'''
while True:
    x,y,m,n,L=map(int,input().split())
    print(date(x,y,m,n,L))