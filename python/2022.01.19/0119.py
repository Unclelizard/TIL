#숫자를 받아서 (인풋)
#세제곱 결과를 반환 (아웃풋)
#ex) 호출 : cube(2), cube(10), cube(100) 결과: 8, 1000, 100000000
# def cube(number):
#     return number ** 3
# print(cube(2))


# def m(x,y):
#     return x - y
#     return x * y #사용 안됨.
# print(m(1,2))


# def rectangle(w,h):
#     return w * h , 2*w + 2*h
# print(rectangle(30,20))


# def rectangle(w,h):
#     area = w * h
#     leng = 2*w + 2*h
#     return area, leng
# print(rectangle(30,20))

# def add(x, y=0):
#     return x+y

# print(add(5,y=20))

# a=10
# def func1():
#     global a
#     a=3

# print(a)
# func1()
# print(a)

# def foo(a, b):
#     return a, b

# print(foo(b=2, a=1))
# from unittest import result


# a=int(input())
# b=int(input())
# def add(a, b):
#     result = a + b
#     return result


# print("%d, %d 합은 %d입니다." %(a,b, add(a,b)))


n,m = map(int, input().split())

print(n + m)