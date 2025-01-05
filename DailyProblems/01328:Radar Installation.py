import math
t=0
while True:
    try :
        n,d=map(int,input().split())
        t+=1
    except ValueError:continue
    if n==0 and d==0:break
    else:
        error=0
        islands=[]
        lines=[]
        for _ in range(n):
            x,y=map(int,input().split())
            islands.append((x,y))
            if abs(y)>d:
                error=1
                continue
            lines.append(((x-math.sqrt(d**2-y**2)),(x+math.sqrt(d**2-y**2))))
        lines.sort(key=lambda x:x[1])
        '''
        nong yige dangqian d start he end point
        '''
        if error==1:
            print(f'Case {t}: -1')
        else:
            i=0
            count=1
            while i < n-1:
                end=lines[i][1]
                while i<n-1 and lines[i][0]<=end :
                    i+=1
                if lines[i][0]>end:
                    end=lines[i][1]
                    count+=1
            print(f'Case {t}: {count}')
