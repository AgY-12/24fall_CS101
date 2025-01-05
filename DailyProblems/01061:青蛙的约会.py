x,y,m,n,L=map(int,input().split())
d0=x-y
dd=m-n
k=d0//L
if dd>0 and d0%L!=0:k+=1
if dd==0:print('Impossible')
elif (L%dd==0 and d0%dd!=0) :
    print('Impossible')
else:
    while (k*L-d0)%dd!=0:
        k+=int(dd/abs(dd))
    a=(k*L-d0)//dd
    print(a)