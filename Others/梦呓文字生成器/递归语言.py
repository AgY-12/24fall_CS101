sentence=input('输入句子:')
s=input('输入要递归的字:')
t=input('输入这个字要变成的内容:')
for j in range(int(input('递归层数:'))):
    sentence=list(sentence)
    for i in range(len(sentence)):
        if sentence[i]==s:
            sentence[i]=t
    sentence=''.join(sentence)
    print(sentence)
'''
for example
input:
悬铃木在下雨
雨
下雨的悬铃木
2

output:
悬铃木在下下下雨的悬铃木的悬铃木

'''