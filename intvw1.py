# Write a function def solution(A)
# that, given an array A of N integers, returns True if A contains at least two
# elements which differ by 1, and False otherwise.
# Examples:
# 1. Given A = [7], the function should return False.
# 2. Given A = [4, 3], the function should return True.
# 3. Given A = [11, 1, 8, 12, 14], the function should return True. Pair of elements
# which differ by 1 is (11, 12).
# 4. Given A = [4, 10, 8, 5, 9], the function should return True. Pairs of elements
# which differ by I are (4, 5), (IO, 9) and (8, 9).
# 5. Given A = [5, 5, 5, 5, 5], the function should return False. There are no two
# elements in A whose values differ by I.
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [1..100,000];
# • each element of array A is an integer within the range

def solution(A):

    first_cond = all(0 < i < 10 ** 9 for i in A)
    sec_cond = 0 < len(A) < 10 ** 5
    if first_cond and sec_cond:
        list_of_pairs = [(x, y) for indx, x in enumerate(A) for y in A[indx + 1:]]
        responses = []
        for pair in list_of_pairs:
            responses.append(abs(pair[0]-pair[1]) == 1)

        if responses.count(True) > 0:
            return True
        return False
    return 'out of range'


print(solution([7]))
print(solution([4, 3]))
print(solution([11, 1, 8, 12, 14]))
print(solution([4, 10, 8, 5, 9]))
print(solution([5, 5, 5, 5, 5]))
