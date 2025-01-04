import math
while True:
    ans=9999999
    n=int(input())
    if n!=0:
        for i in range(n):
            vi,ti=map(int,input().split())
            if ti>=0:
                timei=math.ceil(4500/vi*3.6)+ti
                if timei<ans:
                    ans=timei
        print(ans)
    else:break