class A:
    x = 5
    def __init__(self):
        self.y = 5

class B(A):
    y = 10

a = A()

print('a dict')
for el in a.__dict__:
    print(el)
print(*['-']*10)
print('A dict')
for el in A.__dict__:
    print(el)
print(*['-']*10)
print('a dir')
for el in dir(a):
    print(el)
print(*['-']*10)
for el in object.__dict__h:
    print(el)