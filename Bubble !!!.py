#  Create a function that takes a list of numbers as parameter
#  and returns a list where the elements are sorted in ascending numerical order
#  When you are done, add a second boolean parameter to the function
#  If it is `true` sort the list descending, otherwise ascending

def bubble(arr):
    sorted_arr = []
    for i in range(len(arr)):
        sorted_arr.append(min(arr))
        arr.remove(min(arr))
    return sorted_arr


def advanced_bubble(arr_1, is_descending=True):
    if is_descending:
        sorted_arr = []
        for i in range(len(arr_1)):
            sorted_arr.append(max(arr_1))
            arr_1.remove(max(arr_1))
        return sorted_arr

    else:
        sorted_arr = []
        for i in range(len(arr_1)):
            sorted_arr.append(min(arr_1))
            arr_1.remove(min(arr_1))
        return sorted_arr


print(bubble([43, 12, 24, 9, 5]))
#  should print [5, 9, 12, 24, 34]
print(advanced_bubble([43, 12, 24, 9, 5]))
#  should print [5, 9, 12, 24, 34]
