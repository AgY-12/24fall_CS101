a,b=map(int,input().split())
you=False
c=''
for i in range(a,b+1):
    n=str(i)
    if int(n)==int(n[0])**3+int(n[1])**3+int(n[2])**3:
        you=True
        c+=n+' '
if you==False:print('NO')
else:print(c.rstrip())