num = 10
if num % 2 == 0 :
    print("짝수입니다.")

n=range(1,11)
for i in n:
    print(i)
    
n=range(1,11)
for i in n:
    if i % 2 == 0:
        print("%d는 짝수입니다." %i)
    else:
        print("%d는 홀수입니다." %i)
    
while num>=1:
    print(num)
    num=num-1