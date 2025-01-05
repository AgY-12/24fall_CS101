n=int(input())
i=0
def f(n,p1,p2):
    global i
    if n==1:
        i+=1
        return f'{p1}->{p2}'
    else:
        p2_=list({'A','B','C'}-{p1,p2})[0]
        return f(n-1,p1,p2_)+'\n'+f(1,p1,p2)+'\n'+f(n-1,p2_,p2)
ans=f(n,'A','C')
print(i)
print(ans)