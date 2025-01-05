import random
x=random.randint(1,10000)

for i in range(1,random.randint(1,1000)):
    x+=0.001
    #print(x)
x=((x*1000)//1)/1000
    
count=0
print("我乙腈选了一个1~10000之间的数，可能是整数，也可能是小数。请你猜猜看吧！")
#print("悄悄告诉你，这个数是",x)
while True:
    
    a=input()
    
    if float(a)==x:
        count+=1
        break
    elif float(a)>x:
        print(float(a))
        count+=1
        print("太大了")
    elif float(a)<x:
        print(float(a))
        count+=1
        print("太小了")
print(f"对了！你猜了{count}次")
