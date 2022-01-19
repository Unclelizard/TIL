# 1

map, filter, len, range, max, min, format



# 2

```

def get_middle_char(a):
    name = len(a)
    if name % 2 == 0:
        return a[int(len(a)/2)-1:int(len(a)/2)+1]
    else:
        return a[int(len(a)/2)]
get_middle_char('abcd')
```



# 3.

4

# 4.

none



# 5

```
def my_avg(*args):
    cnt = 0
    sum = 0
    for i in args:
        sum+=i
        cnt+=1
    return sum/cnt
my_avg(100,50,50,100)
```

