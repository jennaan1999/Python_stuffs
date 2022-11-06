from math import sqrt
a = int(input('what is the value of a?'))
b = int(input('what is the value of b?'))
c = int(input('what is the value of c?'))
x1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
print(x1)
x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
print(x2)
