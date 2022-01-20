# 1

```
def get_secret_word(x):
    for num in x:
        
        print(chr(num),end="")
        
get_secret_word([83,115,65])

```



# 2

```
def get_secret_word(x):
    sum=0
    for num in x:
        sum+=int(ord(num))
    return sum
        
get_secret_word('tom')

```



# 3

```
def get_strong_word(x, y):
    sumx=0
    sumy=0
    for num in x:
        sumx+=int(ord(num))
    for num in y:
        sumy+=int(ord(num))
    if sumx > sumy:
        return x
    else:
        return y
get_strong_word('tom','tim')
```

