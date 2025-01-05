
def find(list):
    sum = 0
    sums={}
    for i in range(len(list)):
        a=find(cut(i,list)[0])
        list=list(a[0])
        print(list)
        sums[i]=a[1]
        print(sums)
    print(sums)
    for k,v in sums.items():
        if v==max(sums.values()):
            return v


def cut(k,list):
    sum=0
    print(list)
    del list[0:k]
    i=0
    while i<len(list):
        print('比较：',list[i],list[0])
        if list[i]>list[0]:
            print('砍掉',list[i])
            list.remove(list[i])
            i-=1
        i+=1
    del list[0]
    sum+=1

    return list,sum
n=int(input())
list=list(map(int,input().split()))
print(find(list))
'''
sum=0
while len(list)>1:
    cut(find(list),list)
    print(list)
    sum+=1
sum+=1
print(sum)
'''