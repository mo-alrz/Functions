# map() loops over the items of an input iterable (or iterables) and returns an iterator that results from applying a
# transformation function to every item in the original input iterable.

# Square the list elements
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # It's an object, to print it we have to use the list built-in function

# Int to str and vice versa, abs and ...
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums)
print(list(int_nums))

numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
print(abs_values)

words = ['Hello', 'World', 'Of', 'Python']
print(list(map(len, words)))

# Pow
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]
result = list(map(pow, first_it,second_it))
print(result)

