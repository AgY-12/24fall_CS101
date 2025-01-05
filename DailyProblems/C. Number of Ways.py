'''
3 3 -3 3 -3 3 3
 1 2  1.2  1 2
'''
n=int(input())
a=list(map(int,input().split()))
if sum(a)%3!=0:
    print(0)
else:
    p=[]
    p1=[]
    p2=[]#三分之一点和三分之二点
    count1=count2=0
    s=sum(a)//3
    tmps=0
    for i in range(n-1):
        tmps+=a[i]
        if tmps==2*s:
            p.append((i,2,count2))
            p2.append(i)
            count2+=1
        if tmps==s:
            p.append((i,1,count1))
            p1.append((i,len(p)-1))
            count1+=1
    ans=0
    #print(p,p1,p2)
    for j in range(count1):
        zz=p1[j][1]+1
        while zz<n and p[zz][1]!=2:
            zz+=1
        if zz<len(p):
            #print('指向p中的：',p[zz],'其第二项为',p[zz][2],'指针=',zz)
            #print('ans+=',len(p2)-p[zz][2])
            #print('jia!')
            ans+=len(p2)-p[zz][2]
        #print(p1[j],ans)
    print(ans)

