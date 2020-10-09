x = int(input('Enter your X: '))
y = int(input('Enter your Y: '))
z = 0

while True:
    sign = input('Enter your sign: ')
    if sign == '-' or sign == '+' or sign == '*' or sign == '/':
        break

if sign == '-' or sign == '+' or sign == '*' or sign == '/':
    if sign == '-':
        z = x - y
    if sign == '+':
        z = x + y
    if sign == '*':
        z = x * y
    if sign == '/':
        z = x / y
print(z)
