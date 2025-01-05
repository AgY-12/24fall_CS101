import random
def print_matrix():
    
        for Y in range(1,11):
            for X in range(1,11):
                if X!=10:
                    print(matrix[Y][X],end=' ')
                else:print(matrix[Y][X])
names=[]
xs=[]
ys=[]
count=0
bullet=14
i_s=[]
#,[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' ']
matrix=[[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],[' ','* ','* ','* ','* ','* ','* ','* ','* ','* ','* ',' '],['-','-','-','-','-','-','-','-','-','-','-','-']]
i=1
while i>0:
    print('input names of enemies',i,",input ''OK'' to finish creating enemies:")
    temp=input()
    if temp=='OK':break
    else:
          names.append(temp)
          xs.append(random.randint(1,10))
          ys.append(random.randint(1,10))
    i+=1
print('game starts'+'\n'+'input x and y (bt 1-10) to shoot the enemies\nu have 14 bullets')
print('每一个子弹可以打到周围一圈共9格的敌人')
#打印矩阵
print_matrix()
#print(names)
#print(xs)
#print(ys)
#print(matrix[0][0],matrix[11][0])
#print('haole')
#射击
while(names!=[]):
      shot=0
      i_s=[]
      
      while True:
        try:
                x,y=input('enter x&y:').split()
                x=int(x)
                y=int(y)
        except ValueError:
                print('Look at what you have entered.\nPlease enter again.')
        else:
                break
        

      if x>=1 and x<=10 and y>=1 and y<=10:
          count+=1
          #print(names)
          #print(xs)
          #print(ys)
          #print(x,y)
          #print(matrix[0][0],matrix[11][0])
          #print('haole')
          
          for i in range (len(names)):
              #print('i=',i)
            if x-xs[i]<=1 and y-ys[i]<=1 and x-xs[i]>=-1 and y-ys[i]>=-1:
                    print('u killed '+names[i]+'!')
                    #标记射击点
                    for m in range(y-1,y+2):
                          for n in range(x-1,x+2):
                                if matrix[m][n]=='* ':
                                      matrix[m][n]='o '
                    matrix[ys[i]][xs[i]]='x '
                    #print('haole!')
                    shot=1
                    i_s.append(i)                    
                    #break
                    
                    
          if shot==0:
              print('u killed nobody!')
              #print(x,y)
              #标记射击点
              for m in range(y-1,y+2):
                    for n in range(x-1,x+2):
                          if matrix[m][n]=='* ':
                                matrix[m][n]='o '
#清除敌人
          if shot==1:
              for j in range( len(i_s)-1,-1,-1):
                  del names[i_s[j]]
                  del xs[i_s[j]]
                  del ys[i_s[j]]
#打印矩阵
          print_matrix()
      else:print('out of range.please shoot again.')
      if count>=bullet:break
if count>=bullet and names!=[]:
      print('u lose!')
      print('enemies alive:')
      for i in range(len(names)):
            print(names[i])
else:
      print('u win!')
      print('u shot',count,'times.')
        

