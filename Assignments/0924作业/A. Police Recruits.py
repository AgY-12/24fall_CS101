n=int(input())
a=list(map(int,input().split()))
p=c=0
for i in a:
    if i>0:
      p+=i
    elif p>0:
        p-=1
    else:c+=1
print(c)