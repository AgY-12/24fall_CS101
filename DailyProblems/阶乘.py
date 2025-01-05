def jc(n):
    if n>=2:
        ans=n*jc(n-1)
    elif n==1 or n==0:return 1
    return ans

print(jc(int(input())))