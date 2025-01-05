import math
def Cantor(nums):
    res=0#res是最终的编号
    for i in range(len(nums)):#对于nums中的每个数
        c=0
        for j in range(i+1,len(nums)):#找到它后面有几个比它小的数
            if nums[j]<nums[i]:
                c+=1
        res+=c*math.factorial(len(nums)-1-i)
    return res

def retro_Cantor(x,length):#length是排列的长度,不然我就不知道是123的排列还是1234的排列了
    res=[]
    r=list(range(1,length+1))
    for i in range(length-1,-1,-1):
        f=math.factorial(i)
        res.append(r.pop(x//f))
        x%=f
    return res
def next_arrange(a):
    b=[0]+sorted(a)
    reversed_cast=dict(enumerate(b))#对a中的元素逆映射
    cast={v:k for k,v in reversed_cast.items()}
    cantorable_a=[cast[i] for i in a]
    _=(1+Cantor(cantorable_a))%math.factorial(len(a))
    cantorable_new_a=retro_Cantor(_,len(a))
    new_a=[reversed_cast[i] for i in cantorable_new_a]
    return new_a
print(next_arrange([2,6,4,3]))