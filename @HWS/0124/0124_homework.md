```\
def count_vowels(word):
    sum = word.count('a')+word.count('e')+word.count('i')+word.count('u')+word.count('o')
    return sum

print(count_vowels('aeaai'))
    
```

# 2

4번. 오류가 발생하지않음.



# 3

```
def only_square_area(list1,list2):
    cnt=0
    resultlist=[]				# 총 12번의 비교를 해야한다
    for i in range(len(list1)): #1번리스트의 길이만큼 돌릴것이다. 3번돌림. i는 0,1,2
        for j in range(len(list2)):#2번리스트와 비교하기위해서 2번리스트 길이만큼 돌린다.
        #0-0,0-1,0-2,0-3 ~ 2-3까지 될것이다.
            if list1[i] == list2[j]:#리스트1의 0번값이 리스트2의 0,1,2,3중에 같은값이있다면
                resultlist.append(list1[i]**2)#새로운리스트에 값을 제곱해서 넣어준다.
       
    return resultlist
                
    
    
    
print(only_square_area([32,55,63], [13,32,40,55]))
```

