import bisect
import math

n=int(input())
fr=list(map(int,input().split()))

fr.sort()
position4=bisect.bisect_left(fr,4)
position3=bisect.bisect_left(fr,3,0,position4)
position2=bisect.bisect_left(fr,2,0,position3)
count4=len(fr)-position4
count3=position4-position3
count2=position3-position2
count1=len(fr)-count4-count3-count2
#print(count4,count3,count2)
taxi=count4+count3+math.ceil(count2/2)+max(math.ceil((count1-count3-(count2%2)*2)/4),0)
'''
count4=fr.count(4)
count3=fr.count(3)
count2=fr.count(2)
count1=fr.count(1)
'''
taxi=count4+count3+math.ceil(count2/2)+max(math.ceil((count1-count3-(count2%2)*2)/4),0)
print(taxi)