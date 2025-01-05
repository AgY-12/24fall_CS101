n=int(input())
week=['Sun','Mon','Tues','Wednes','Thurs','Fri','Satur']
data=[]
for i in range(n):
    line=input()
    m=int(line[4:6])
    cy=int(line[0:4])

    if m==1 or m==2:
        cy-=1
        m+=12
    cy=str(cy)
    c=int(cy[0:2])
    y=int(cy[2:4])

    d=int(line[6:8])
    w=(y+int(y/4)+int(c/4)-2*c+int(2.6*(m+1))+d-1)%7
    data.append(w)
for i in data:
    print(week[i]+'day')