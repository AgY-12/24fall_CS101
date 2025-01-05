c=int(input())
d=int(input())
a=list(str(c))
b=list(str(d))
a.reverse()
b.reverse()
ans=[0 for i in range(202)]
while len(a)<len(b):
    a.append('0')
while len(b)<len(a):
    b.append('0')

for j in range(max(len(b),len(a))):
        ans[j]+=(int(b[j])+int(a[j]))%10
        ans[j+1]+=(int(a[j])+int(b[j]))//10
        ans[j+1]+=(ans[j])//10
        ans[j]%=10
i=0
while i==0 and ans:
    i=ans.pop()
ans.append(i)
ansstr=''
for i in ans[-1::-1]:
    ansstr+=str(i)
print(int(ansstr))
print(c+d)
