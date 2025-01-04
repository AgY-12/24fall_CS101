import sys
pigs=[]
dstack=[]
def push(n):
    pigs.append(n)
    if not dstack or pigs[dstack[-1]]>n:
        dstack.append(len(pigs)-1)
def popa():
    if pigs:
        if len(pigs)-1==dstack[-1]:
            dstack.pop()
        pigs.pop()
def min():
    if pigs:
        #print(pigs)
        #print(dstack)
        return pigs[dstack[-1]]

lines=sys.stdin.read().split()
#print(lines)
i=0
while i<len(lines):
    line=lines[i]
    if 'push' in line:
        i+=1
        line=lines[i]
        push(int(line))
    if 'pop' in line:
        popa()
    if 'min' in line and pigs:
        print(min())
    i+=1