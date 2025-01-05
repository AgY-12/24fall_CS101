a=input()
a=str(ord(a))
print(a)
a=a[::-1]
a.lstrip('0')
print(a)
a=chr(int(a))
print(a)
'''
for example:
input:独
output:
29420
02492
়
'''