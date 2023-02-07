# - Create a function called `calculateFactorial()`
#   that returns the factorial of its input

def factorial(x):
    factorial_x = 1
    for i in range(1, x + 1):
        factorial_x *= i
    return factorial_x


print(factorial(5))
