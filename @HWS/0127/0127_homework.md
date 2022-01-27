# 1

```
class Circle:
    pi = 3.14
    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    def area(self):
        return Circle.pi* self.r *self.r
    def circumference(self):
        return 2 * Circle.pi * self.r
    def center(self):
        return (self.x, self.y)
a=Circle(3,2,4)
print(a)
print(a.area())
print(a.circumference())
print(a.center())

```

```python
class Animal:
	def __inint__(self, name):
		self.name=name
	def walk(self):
		print(f'{self.name}1 걷는다!')
	def eat(self):
		print(f'{self.name}! 먹는다!')
class Dog(Animal):
	def walk(self):
		print(f'{self.name}! 달린다!')
	def bark(self):
		print(f'{self.naem}! 짖는다!')
		
```

