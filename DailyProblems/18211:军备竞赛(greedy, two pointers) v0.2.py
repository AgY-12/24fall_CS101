'''
1：经费不够做武器：
    1-1武器数一样多：ans=0
    1-2武器更多：如果卖了一件最贵的够做，就卖(但是你只剩一件武器就不能卖了）；否则ans不动了
2：经费够做武器：
    2-1 武器一样多：做
    2-2 武器更多：做！没必要卖（因为你现在卖跟钱不够了再卖没区别）
'''
p=int(input())
weapons=list(map(int,input().split()))
weapons.sort()
ans=0
while len(weapons)>1:
    #print('p:',p,'weapons:',weapons)
    if p<weapons[0]:
        if ans==0:
            print(ans)
            break
        else:
            if p+weapons[-1]>=weapons[0] and len(weapons)>1:
                p+=weapons.pop()
                ans-=1
    if p>=weapons[0]:
        p-=weapons[0]
        weapons=weapons[1:]
        ans+=1
else:print(ans)
