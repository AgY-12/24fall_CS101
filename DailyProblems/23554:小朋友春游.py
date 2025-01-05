n=int(input())
list=list(map(int,input().split()))
ispresent=[False for _ in range(n+1)]
for i in range(1,n+1):
    if i in list:
        ispresent[i]=True
        list.remove(i)
    if ispresent[i]==False:
        print(i,end=' ')
print('')
list.sort()
for i in list:
    print(i,end=' ')