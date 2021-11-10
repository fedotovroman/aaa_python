from math import pi

class Circle1:
    def __init__(self, x = 0, y = 0, r = 1):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return pi * self.r**2

    def perimetr(self):
        return 2 * pi * self.r

    def zoom(self, k):
        self.r *= k

    def is_crossed(self, c):
        d2 = (self.x - c.x)**2 + (self.y - c.y)**2
        r2 = (self.r + c.r)**2
        return d2 <= r2

    def __str__(self):
        return 'Circle x = {}, y = {}, r = {}, area = {} '.format(self.x, self.y, self.r, self.area())


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self._y = y
        self.__r = r

    def set_r(self, r):
        if r < 0:
            raise ValueError(f'radius {r} < 0')
        self.__r = r

    def __str__(self):
        return 'Circle x = {}, y = {}, r = {} '.format(self.x, self._y, self.__r)

c1 = Circle(1,2,3)

c1.__r = 100


class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Rect():
    def __init__(self, x = 0, y = 0, w = 0, h = 0):
        self.lt = Point(x,y)
        self.width = w
        self.height = h

import copy

p1 = Point(1,2)
p2 = copy.copy(p1)


r1 = Rect(0,0, 100, 100)
r2 = copy.copy(r1)
r3 = copy.deepcopy(r1)

class Thing:
     def __init__(self,**kwargs):
         for k,v in kwargs.items():
             setattr(self,k,v)
     def __getitem__(self,item):
         return self.__dict__.get(item,None)
     def __repr__(self):
         return "<Thing: %s>"%self.__dict__

t = Thing(**json.loads('{"name":"Bogdan","age":"21","sex":"male"}'))