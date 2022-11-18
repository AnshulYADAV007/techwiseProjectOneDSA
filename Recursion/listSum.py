# This function returns the sum of all the elements of the lst
def listSum(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + listSum(lst[1:])


print(listSum([1, 2, 3, 4, 5, 6, 7, 8]))

# [1] -> 1 -> (1 * 2)/2
# [1,2] -> 3 -> (2 * 3)/2
# [1,2,3] -> 6 -> (3 * 4)/2
# [1,2,3,4] -> 10 -> (4 * 5)/2
# [1,2,3,...,n] -> (n * (n + 1)) / 2
# listSum(range(10))
