n=input()
n=int(n)
#ru=[]
for i in range(n):
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    x_1=(b*-1+(b*b-4*a*c)**0.5)/(2*a)
    x_2=(b*-1-(b*b-4*a*c)**0.5)/(2*a)

    #ru.append(x_1)
    #ru.append(x_2)
    if x_1==x_2:
        #print(f'x1=x2={'{:.5f}'.format(x_1)}')
        print('x1=x2='+str(int(x_1*100000)/100000))
    elif x_1!=x_2 and x_1.imag==0:
        #print(f'x1={'{:.5f}'.format(x_1)};x2={'{:.5f}'.format(x_2)}')
        print('x1='+str(int(x_1*100000)/100000)+', x2='+str((int(x_2*100000)/100000)))
    else:
        print(f'x1={'{:.5f}'.format(x_1.real)}+{'{:.5f}'.format(x_1.imag)}i;x2={'{:.5f}'.format(x_2.real)}{'{:.5f}'.format(x_2.imag)}i')
        print('x1='+str(int(x_1.real*100000)/100000)+'+'+str(int(x_1.imag*100000)/100000)+'i,x2='+str(int(x_2.real*100000)/100000)+'+'+str(int(x_2.imag*100000)/100000)+'i')
