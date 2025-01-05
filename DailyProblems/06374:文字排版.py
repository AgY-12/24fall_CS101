n=int(input())
text=input().split()
pr=[]
length=0
i=0
while i < len(text):
    while True:
        length+=len(text[i])+1
        pr.append(text[i])
        i+=1
        if (length<=81 and i<len(text))==False:
            break
    temp=pr.pop()
    while len(pr)>=2:
        print(pr.pop(0),end=' ')
    if i !=len(text):
        print(pr.pop())
        pr.append(temp)
        length=len(temp)+1
    elif i == len(text):
        pr.append(temp)
        print(pr.pop(0),end=' ')
        print(pr.pop(0),end='')
