def zhuang(a,b,c,d,e,f):
    num=f
    f=0
    #print(a,b,c,d,e,num)
    num+=e
    a=max(a-11*e,0)
    e=0
    #print(a, b, c, d, e, num)

    num+=d
    temp=b
    b=max(b-5*d,0)
    b_subtract=temp-b
    a=max(a - (20*d-b_subtract*4),0)
    d=0
    #print(a, b, c, d, e, num)

    num+=c//4
    c=c%4
    if c>0:
        num+=1
        temp=b
        b=max(b-(7-2*(c)),0)
        b_subtract=temp-b
        a=max(a-(36-9*(c)-4*b_subtract),0)
        c=0
    #print(a, b, c, d, e, num)

    num+=b//9
    b=b%9
    while a>0 or b>0:
        num+=1
        a=max(a-(36-4*(b)),0)
        b=0
        #print(a, b, c, d, e, num)
    return num


while True:
    a,b,c,d,e,f = map(int,input().split())
    if (a,b,c,d,e,f) != (0,0,0,0,0,0):
        print(zhuang(a,b,c,d,e,f))

    else:break