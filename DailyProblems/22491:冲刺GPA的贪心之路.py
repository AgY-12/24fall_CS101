h=int(input())
m=int(input())
t=2*h-0.5*m
courses=[]
for i in range(m):
    sc=list(map(float,input().split()))
    sc.append(sc[0]*sc[1])
    courses.append(sc)
courses.sort(key=lambda x:x[2],reverse=True)
xfj=0
i=0
while t>0 and i<len(courses):
    ti=min(t,5/courses[i][0])
    t-=ti
    xfj+=courses[i][0]*ti*courses[i][1]
    i+=1
print(round(xfj,1))
