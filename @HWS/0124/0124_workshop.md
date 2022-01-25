# 1

```
def get_dict_avg(abc):
    a=abc.values()
    sum=0
    for i in a:
        sum+=i
    return sum/len(a)
    
    
get_dict_avg({'python': 80,'algorithm': 90,'django': 89,'web': 83})    

abc의 밸류값들을 저장해준다
평균구함

```

# 2

```
def count_blood(abcab):
    resultdic={}
    resultdic['A']= abcab.count('A')
    resultdic['B']= abcab.count('B')
    resultdic.update(O=abcab.count('O'))
    resultdic.update(AB=abcab.count('AB'))
    return resultdic
    
    
count_blood(['A','B','A','O','AB','AB','O','A','A','B','O','B','AB'])

```

```
blood_type=(['A','B','A','O','AB','AB','O','A','A','B','O','B','AB'])
#모든 요소를 순회한다.
result={}
for blood_type in blood_types:
	#딕셔너리에 키가 있으면:..
	if blood_type in result:
		result[blood_type] +=1
	else:
		result[blood_type] = 1
	#딕셔너리에 키가 없으면:
```

