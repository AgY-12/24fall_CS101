t=0
while True:
    t+=1
    p,e,i,d=map(int,input().split())
    if p==e==i==d==-1:break
    else:
        a=set(p+k for k in range(0,21252+d-p+1,23))
        b=set(e+k for k in range(0,21252+d-e+1,28))
        c = set(i + k for k in range(0, 21252+d - i + 1, 33))
        Ans=a&b&c
        ans=33333
        for i in Ans:
            if i >d and i<ans:
                ans=i
        print(f'Case {t}: the next triple peak occurs in {ans-d} days.')