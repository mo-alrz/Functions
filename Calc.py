import sys

my_list = sys.argv[1]


def calculator(a, b, c):
    if a == '-':
        print(int(b) - int(c))
    if a == '*':
        print(int(b) * int(c))
    if a == '+':
        print(int(b) + int(c))
    if a == '/':
        print(int(b) / int(c))
    if a == '%':
        print(int(b) % int(c))


calculator(*my_list)