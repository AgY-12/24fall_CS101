from itertools import count

n=input()
n=int(n)
coins={}
for i in range(ord('A'),ord('L')+1):
    coins[chr(i)]=2#2表示重量未知，0表示重量正常
for zu in range(n):
    for ci in range(3):
        ls,rs,w=input().split()
        if w=='even':
            for i in ls:
                coins[i]=0
            for i in rs:
                coins[i]=0
        elif w=='up':
            for i in ls:
                if coins[i]==2:
                    coins[i]='heavy'
                elif coins[i]=='light':
                    coins[i]=0
            for i in rs:
                if coins[i] == 2:
                    coins[i] = 'light'
                elif coins[i] == 'heavy':
                    coins[i] = 0
                elif coins[i]=='light':
                    temp=0
                    for j in ls:
                       if coins[j]!=0:
                           temp+=1
                    if temp==0:
                        for p in range(ord('A'), ord('L') + 1):
                            if p not in rs:
                                coins[chr(p)] =0
                        coins[i]='light'

        elif w=='down':
            for i in ls:
                if coins[i] == 2:
                    coins[i] = 'light'
                elif coins[i] == 'heavy':
                    coins[i] = 0
            for i in rs:
                if coins[i]==2:
                    coins[i]='heavy'
                elif coins[i]=='light':
                    coins[i]=0
                elif coins[i]=='heavy':
                    temp=0
                    for j in ls:
                       if coins[j]!=0:
                           temp+=1
                    if temp==0:
                        for p in range(ord('A'), ord('L') + 1):
                            if p not in rs:
                                coins[chr(p)] =0
                        coins[i]='heavy'
    for k,v in coins.items():
        if v=='light' or v=='heavy' :
            print(k,'is the counterfeit coin and it is',v)
#budui
