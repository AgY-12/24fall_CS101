while True:
    line=input()
    for i in line:
        #print(i,end="")
        i=chr(ord(i)*4)
        print(i,end='')
    print('')
'''
for example:
input:乱码,abc
output:𓧄𞀄°Ƅƈƌ
'''