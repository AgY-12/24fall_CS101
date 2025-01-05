dp3=[0]*14
dp4=[0]*14
for i in range(1,13):
    dp3[i]=2*dp3[i-1]+1
    for j in range(0,i+1):
        tmp=2*dp4[j]+dp3[i-j]
        if dp4[i]==0 or tmp<dp4[i]:
            dp4[i]=tmp
for i in range(1,13):
    print(dp4[i])
