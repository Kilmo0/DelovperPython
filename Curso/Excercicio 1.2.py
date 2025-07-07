a,b,c = 1, 2, 3

print(b)

a = b = c = 1
print(a, b, c)

x = y = [7, 8, 9]
x = [13, 14, 15]
print(x)

print('-'*20)

x = y = [7, 8, 9]
x[0] = 13
print(x)

x = [1, 2, [3, 4, 5], 6, 7]
print(x[2][1])