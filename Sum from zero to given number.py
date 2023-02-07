# Write a function called `sum()` that returns the sum of
# numbers from zero to the given parameter

def sum_zero_to_given_number(number):
    total = 0
    for i in range(number+1):
        total += i
    return total


print(sum_zero_to_given_number(5))
