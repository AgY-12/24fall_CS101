n=input()
dec=0
for i in range(len(n)):
    dec+=int(n[i*-1-1])*(2**(i))
print(dec)