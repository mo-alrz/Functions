my_sum = lambda x: x + 1
print(my_sum(5))

my_multiply = lambda x, y: x * y
print(my_multiply(5, 3))


def myfunc(n):
    return lambda a: a * n


my_doubler = myfunc(2)
print(my_doubler(11))

ret = lambda x: x
print(ret(5))


def func_compute(n):
    return lambda x: x * n


first = func_compute(2)
print(first(15))

tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
tuples.sort(key=lambda x: x[1])
print(tuples)

list_one = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
            {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_list = sorted(list_one, key=lambda x: x['make'])
print(sorted_list)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [i for i in a if i % 2 == 0]  # List comprehension
odd = [i for i in a if i % 2 != 0]

even_2 = list(filter(lambda x: x % 2 == 0, a))  # Lambda
odd_2 = list(filter(lambda x: x % 2 != 0, a))

print(even, odd)
print(even_2, odd_2)

square = [i ** 2 for i in a]  # List comprehension
cube = [i ** 3 for i in a]

square_1 = list(map(lambda x: x ** 2, a))  # Lambda
cube_1 = list(map(lambda x: x ** 3, a))

print(square, cube)
print(square_1, cube_1)

import datetime

now_time = datetime.datetime.now()
print(now_time)

year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now_time))
print(month(now_time))
print(day(now_time))
print(t(now_time))

is_num = lambda x: x.replace('.', '', 1).isdigit()
print(is_num('4.2'))
