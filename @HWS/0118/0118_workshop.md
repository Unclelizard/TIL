# 1번

```
a=int(input())
number=0
for mod in range(1,1001):
    number=number+1
    if a % mod == 0:
        print(number, end=" ")
```





# 2번

```
numbers =[ 85, 72, 38, 80, 69, 65, 68, 96, 22,10,11]

numbers.sort()

if len(numbers) % 2 == 1:
    print(numbers[int(len(numbers) / 2) +1])
    print(numbers[int(len(numbers) / 2) -1])

else:
    print(numbers[int(len(numbers) / 2)])
    
```





# 3번



```python
a=int(input())

for i in range(1,a+1):
    for j in range(1,i+1): #ex 4일때 i가 도는 레인지는 1,2,3 1번일때 다시 j가 도는것은 레인지 1,2 
        print(j,end="")	#그러면 참조하는 값은 1이고 프린트1,출력후 포문밖에서 공백출력
    print()				#다시 2가돌때 J가는 범위 1,2,3을 참조하고 1,2만 출력, 
    
```

