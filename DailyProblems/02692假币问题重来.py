n=input()
n=int(n)
coins = {}
for zu in range(n):
    for i in range(ord('A'), ord('L') + 1):
        coins[chr(i)] = 0  # 0表示重量未知
    data = []
    #print(coins)
    for ci in range(3):
        ls,rs,w=input().split()
        ls=list(ls)
        rs=list(rs)
        data.append([ls,rs,w])
        #print(data)
    #print(data[1])
    for ii in range(ord('A'),ord('L')+1):
        i=chr(ii)
        for j in range(3):
            if (i in data[j][0] or i in data[j][1]) and data[j][2]=='even':
                coins[i]='real'
            elif (i in data[j][0] or i in data[j][1]) and data[j][2]=='up':
                if i in data[j][0]:
                    if coins[i] in[0,1,2]:coins[i]+=1
                    elif coins[i] in[-1,-2]:coins[i]='real'
                elif i in data[j][1]:
                    if coins[i] in[0,-1,-2]:coins[i]-=1
                    elif coins[i] in[2,1]:coins[i]='real'
            elif (i in data[j][0] or i in data[j][1]) and data[j][2]=='down':
                if i in data[j][1]:
                    if coins[i] in[0,1,2]:coins[i]+=1
                    elif coins[i] in[-1,-2]:coins[i]='real'
                elif i in data[j][0]:
                    if coins[i] in[0,-1,-2]:coins[i]-=1
                    elif coins[i] in[2,1]:coins[i]='real'
        if coins[i]==3:
            coins[i]='heavy'
        if coins[i]==-3:
            coins[i]='light'
    #print(coins)
    if 'heavy' in coins.values() or 'light' in coins.values():
        for k,v in coins.items():
            if coins[k]=='heavy'or coins[k]=='light':
                print(k, 'is the counterfeit coin and it is',coins[k]+'.')
    elif 2 in coins.values() or -2 in coins.values():
        for k, v in coins.items():
            if coins[k] == 2:coins[k]='heavy';
            if coins[k] == -2:coins[k]='light';
            if coins[k] == 'heavy' or coins[k] == 'light':
                print(k, 'is the counterfeit coin and it is',coins[k]+'.')
    elif 1 in coins.values() or -1 in coins.values():
        for k in coins.keys():
            if coins[k] == 1:coins[k]='heavy';
            if coins[k] == -1:coins[k]='light';
            if coins[k] == 'heavy' or coins[k] == 'light':
                print(k, 'is the counterfeit coin and it is',coins[k]+'.')