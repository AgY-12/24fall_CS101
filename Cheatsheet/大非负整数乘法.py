#大非负整数乘法
def times(a,b):
    a,b=list(str(a)),list(str(b))
    a.reverse()
    b.reverse()
    ans=[0 for i in range(10002)]
    for j in range(len(b)):
        for i in range(len(a)):
            ans[j+i]+=int(b[j])*int(a[i])%10
            ans[j+i+1]+=ans[j+i]//10
            ans[j+i]%=10
            ans[j+i+1]+=int(b[j])*int(a[i])//10
    i=0
    while i==0 and ans:
        i=ans.pop()
    ans.append(i)
    res=''
    for i in ans[-1::-1]:
        res+=str(i)
    return int(res)

print(times(13**100,13**400))

