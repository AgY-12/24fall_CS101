m,n,a=input().split()
m,n,a=int(m),int(n),int(a)
if m//a==m/a:
    x=m/a
else:
    x=m//a+1
if n//a==n/a:
    y=n/a
else:
    y=n//a+1
x,y=int(x),int(y)
print(x*y)