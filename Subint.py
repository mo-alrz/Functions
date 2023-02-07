#  Create a function that takes a number and a list of numbers as a parameter
#  and returns the indices of the numbers of the list which contain the given number
#  or returns an empty list (if the number is not part of any numbers in the list)


def find_matching_indexes(x,my_list):
    indexes = []
    for i in my_list:
        for j in str(i):
            if str(x) in j:
                indexes.append(my_list.index(i))
                break
    return indexes


print(find_matching_indexes(1, [1, 11, 34, 52, 61]))
# should print: `[0, 1, 4]`
print(find_matching_indexes(9, [1, 11, 34, 52, 61]))
# should print: '[]'






