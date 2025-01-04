n,d=map(int,input().split())
hs=[]
for i in range(n):
    hs.append(int(input()))
mins=[]
i=0
maxi=0
mini=1000000009
while i <len(hs):
    it=i#cun yi xia i de zhi
    #print('it,i,maxi,mini:',it,i,maxi,mini)

    #print('panduan:hs[it],maxi,mini:',hs[it],maxi,mini)
    maxi=max(hs[it],maxi)
    mini=min(hs[it],mini)
    while True:
        #print('hs[it],maxi,mini bianwei:',hs[it],maxi,mini)
        if hs[i]>=maxi and hs[i]-mini<=d:
            mins.append(hs[i])
            hs[i]=-1
            #print('mins:', mins)
            break
        if hs[i]<maxi :
            if maxi - hs[i] <= d and abs(hs[i]-mini)<=d:#zi you dian
                mins.append(hs[i])
                hs[i]=-1
                #print('mins:',mins)
                break
            elif (hs[i]<hs[i-1] and hs[i-1]-hs[i]<=d) or hs[i-1]==-1:
                hs[i],hs[i-1]=hs[i-1],hs[i]
                i -= 1
                #print(hs)
            else:break
        else:break
        if i ==0: break
    i = it + 1
mins.sort()
for i in mins:print(i)
#print(hs,mark)
for i in range(len(hs)):
    if hs[i]!=-1:
        print(hs[i])
'''
10 5
1
6
2
7
3
8
1
6
2
7

10 3
9
8
7
6
9
8
7
6
5
4
问题：只选出了第一轮自由点、
后面的还得硬排
优化见“OJ刷”
'''
