L = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def sum_up_diagonals(L):
    total = 0
    for i in range(len(L)):
        total += L[i][i]
        total += L[i][-1 - i]
    return total


# print(L[i][-1 - i])....-1 = the last element of the nested list.
# Therefore -1 at each index equals 3, 6, and 9.
# When you subtract the -1 index (3,6,9) by the index of the nested list (0,1,2)
# You get 3-0 = 3 // 6-1 = 5 // 9-2 = 7
