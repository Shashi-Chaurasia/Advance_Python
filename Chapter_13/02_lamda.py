
# def func(a):
#     return a + 5


# a = 9
# print(func(a))

func = lambda x: x + 5
sum = lambda x , a, b, c: x + a + b + c
square = lambda x: x**2
cube = lambda x: x**3
x = 5

print(func(x))
print(sum(x , 3, 4, 5))
print(square(x))
print(cube(x))