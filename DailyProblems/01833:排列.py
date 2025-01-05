def bisect_left(a, x,):
    lo,hi=0,len(a)
    while lo < hi:
         mid = (lo + hi) // 2
         if a[mid] > x:
             lo = mid + 1
         else:
            hi = mid
    return lo

n=int(input())
for _ in range(n):
    m,k=map(int,input().split())
    string=list(map(int,input().split()))
    #print(string)
    i=0
    while i<k:
        p=-1
        while p+len(string)>0:
            #print('str:',string)
            #print('i,p',i,p)
            if string[p-1] < string[p]:

                #zhao dao zuixiao d  bi wo da d shu
                exc=bisect_left(string[p::],string[p-1])-1+p
                #print('exc:',exc)
                #print('diao:',string[p-1] , string[exc])
                string[p-1],string[exc]=string[exc],string[p-1]
                #print('exchou:',string)
                string[p::]=sorted(string[p::])
                #print('paixuhou:',string)
                i+=1
                break
            else:p-=1
        else:
            string.reverse()
            i+=1
    print(*string,sep=' ')

