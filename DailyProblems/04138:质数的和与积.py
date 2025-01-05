def isprime(a):
    for i in range(2,int(a**0.5)+1):
        if a%i==0:return False
    return True
s=int(input())
if s%2!=0:
    print(2*(s-2))
else:
    j=s//2
    while isprime(j)==False or isprime(s-j)==False and j<s:
        if j%2==0:j+=1
        else:j+=2
    print(j*(s-j))