#一直R遇到单个B就翻,一直B遇到单个R也翻

rose=list(input())
ans=0
id=0
if len(rose)>=2 and rose[0]=='B' and rose[1]=='R':
    ans+=1
    id+=1
start={'idx':id,'color':rose[id]}
while id<len(rose):
    while id < len(rose) and start['color']==rose[id]:
        id+=1
    if (id+1<len(rose) and rose[id]!=rose[id+1]):
        ans+=1
        #print('但')
        id+=1
    else:
        if id==len(rose)-1 and rose[int(id)]=='B':
            ans+=1
            id+=1
            #print('单个')
        if start['color']=='B':
            #print(start)
            ans+=2
            #print('B')
            if start['idx']==0:
                ans-=1
                #print('走上来的B')
        if id<len(rose):
            start={'idx':id,'color':rose[id]}
print(ans)



