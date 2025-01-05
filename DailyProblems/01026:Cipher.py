def find(i):
    #对每位明文，将加密的循环周期建立一个列表，列表中的第i（从1开始计）项是第i次加密后指向的在密文中的位置
    jiamicishu = 1
    pointer = [key[i]]
    while (len(pointer) == 1 or pointer[-1] != pointer[0]) and jiamicishu <= k:
        pointer.append(key[pointer[-1] - 1])
        jiamicishu += 1
    pointer.pop()
    # if code[i]=='d':
    # print(pointer,len(pointer))
    if len(pointer) == 0:
        pointer_final = key[i]
    else:
        pointer_final = pointer[(k - jiamicishu) % len(pointer)]
    return pointer_final
while True:
    n=int(input())
    if n!=0:
        key=list(map(int,input().split()))#输入密钥
        while True:
            k=input().split(' ',1)
            if k[0]!='0':
                code=(k[1])#输入加密总次数和明文
                #print(n,len(code),n-len(code))
                for _ in range(n-len(code)):code+=' '#补齐空格
                #print(code)
                k=int(k[0])#提取加密总次数
                #print(k)
                tmp=[''for _ in range(len(code))]#建立临时列表 用于存储最终加密后的密文
                #print(tmp)
                #对每个字符一边加密一边寻找周期，找到周期后
                for i in range(len(code)):
                    tmp[find(i)-1]=code[i]
                code=''.join(tmp)
                print(code)
            else:
                print()
                break
    else:break
