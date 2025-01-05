while True:
    try:
        mail=input()
        if mail.count('@')==1 and mail[0]!='@' and mail[0]!='.' and mail[-1]!='@' and mail[-1]!='.' and '@.' not in mail and '.@' not in mail:
            a=False
            for i in mail:
                if i=='@':a=False
                if i=='.':a=True
            if a==False:print('NO')
            else:print('YES')
        else:print('NO')
    except EOFError:break