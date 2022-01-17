### input받기
from this import d


# a=input()
# input() 받은것은 문자열(str) a=b 비교불가
# 따라서 a=int(input())
# n=1로 놓고
# %d 번째 로또 : %n


import random
print("몇 번 살래?")
a=int(input())
b=1
n=1
while a >= b:
    print(("%d 번째 로또는 :"%n),sorted(random.sample(range(1,46),6)))
    b+=1
    n+=1

    
    
       
    

        


    
    
    



# import random
# print(sorted(random.sample(range(1,46),6)))


    
# print(n)

   
# import random


# print(sorted(random.sample(range(1,46),6)))
