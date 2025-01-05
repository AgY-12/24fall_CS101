n,wm=map(int,input().split())
vm=0
bag=0
candy=[]
for i in range(n):
    v,w=map(int,input().split())
    candy.append((v,w,v/w))
    try:
        j=-1
        while(candy[j-1][2]<candy[j][2]):
            t=candy[j-1]
            candy[j-1]=candy[j]
            candy[j]=t
            j-=1
    except IndexError:continue
for i in candy:
    vm+=min(i[1],wm-bag)*i[0]/i[1]
    bag+=min(i[1],wm-bag)
    if bag==wm:break
print(round(vm,1))