def a(x):
    return b(x)
def b(x):
    return a(x)
print(a(1))
'''
无穷死循环递归,别跑...
'''