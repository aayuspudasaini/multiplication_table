# Multiplication table (from 1 to n) in Python
# To take input from user
num = int(input("Display Multiplication table of ? "))
n = int(input("No. of iterate: "))
# Iterate n times from i = 1 to n
print(f'Multiplication table of {num}')
for i in range(1, n + 1):
    print(num, 'x', i, '=', num * i)
