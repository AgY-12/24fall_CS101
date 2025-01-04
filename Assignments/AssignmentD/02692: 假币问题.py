from collections import deque
n=int(input())
for _ in range(n):
    coins={}
    for i in range(ord('A'),ord('L')+1):
        coins[chr(i)]=0# 0=weizhi, '0'=zhengchang,1=zhongle, -1=qingle
    weigh=deque([])
    for i in range(3):
        line=list(input().split())
        if line[2]=='even':
            weigh.appendleft(line)
        else:weigh.append(line)
    for line in weigh:
        if line[2]=='even':
            for i in line[0]:coins[i]='0'
            for i in line[1]:coins[i]='0'
        elif line[2]=='up':
            for i in line[0]:
                if coins[i]!='0':coins[i]+=1
                if coins[i]==0:coins[i]='0'
            for i in line[1]:
                if coins[i]!='0':coins[i]-=1
                if coins[i] == 0: coins[i] = '0'
        elif line[2]=='down':
            for i in line[1]:
                if coins[i]!='0':coins[i]+=1
                if coins[i]==0:coins[i]='0'
            for i in line[0]:
                if coins[i]!='0':coins[i]-=1
                if coins[i] == 0: coins[i] = '0'
        if line[2]!='even':
            for i in set(coins.keys())-(set(line[0])|set(line[1])):coins[i]='0'
    for i in coins:
        if coins[i]=='0':coins[i]=0
    #print(coins)
    for coin in coins:
        if coins[coin]>0 and coins[coin]==max(coins.values()):
            print(f'{coin} is the counterfeit coin and it is heavy. ')
        if coins[coin]<0 and coins[coin]==min(coins.values()):
            print(f'{coin} is the counterfeit coin and it is light. ')
