def issign(a):
    if a in ('+','-','*','/'):return True
    return False
def cal(a,l,r):
    if a == '+':
        return l + r
    elif a == '-':
        return l - r
    elif a == '*':
        return l * r
    elif a == '/':
        return l / r

def Pol():
    global f
    if not issign(f[0]):
        return f.pop(0)
    else:
        sign,left,right=f.pop(0),[],[]
        left=Pol()
        right=Pol()
        return(cal(sign,left,right))


f=list(input().split())
for _ in range(len(f)):
    if not issign(f[_]):f[_]=float(f[_])
print('{:.6f}'.format(Pol()))
