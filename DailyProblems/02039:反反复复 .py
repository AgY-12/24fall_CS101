n=int(input())
list=list(input())
a=[]
l=int(len(list)/n)
for i in range(l):
    if i%2==0:
        a.append(list[0:n])
    else:
        a.append(list[n-1::-1])
    del list[0:n]
while a[0]:
    for i in a:
        print(i.pop(0),end='')