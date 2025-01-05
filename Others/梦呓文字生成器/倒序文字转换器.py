line=[]
while l:=list(input()):
    line+=l
line.reverse()
print(*line,sep='')
'''
for example:
input:世界是一场盛大的Wrong Answer
output:rewsnA gnorW的大盛场一是界世
'''