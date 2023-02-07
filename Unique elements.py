#  Create a function that takes a list of numbers as a parameter
#  and returns a list of numbers where every number is unique (occurs only once)

def find_unique_items(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(find_unique_items([1, 11, 34, 11, 52, 61, 1, 34]))
#  should print: [1, 11, 34, 52, 61]



