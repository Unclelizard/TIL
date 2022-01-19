# 1

```

def list_sum(a):
    sumlist=0
    for i in a:
        sumlist += i
    return print(sumlist)
list_sum([1,2,3,4,5])

```



# 2



# 3

```
def all_list_sum(lst):
    res=0
    for i in lst:
        if type(i)==list:
            res+=all_list_sum(i)
        else:
            res+=i
    return res

all_list_sum([[1],1,[1,1,1],[1,1]])
```

