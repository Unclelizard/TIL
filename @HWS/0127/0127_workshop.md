# 1

```
class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
class Rectangle:
    
    def __init__(self, p1, p2):
        # p1 - (1, 3)
        # p2 - (3, 1)
        self.p1 = p1
        self.p2 = p2
    def get_area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)
        
    @property
    def area(self):
        return (self.p2.x - self.p1.x) * (self.p1.y - self.p2.y)
    
get_area()
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.area)
```

