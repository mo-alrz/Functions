# - Create a function called `print_params`
#   which prints the input parameters
#   (can have multiple number of arguments)


def all_parameters(a, b, c):
    for k, v in locals().items():
        print(v)


all_parameters([1, 2, 3], 1, 'r')
