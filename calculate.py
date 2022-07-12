import sys


a = int(sys.argv[1])
b = int(sys.argv[3])
c = sys.argv[2]

if c == '+':
    print(a + b)

elif c == '-':
    print(a - b)

elif c == '*':
    print(a * b)

elif c == '/':
    print(int(a / b))
