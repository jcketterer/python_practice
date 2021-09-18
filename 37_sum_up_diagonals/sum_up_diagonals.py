def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    total = 0

    for idx in range(len(matrix)):
        # print(matrix[idx][idx], [-1 - idx])
        total += matrix[idx][idx]
        total += matrix[idx][-1 - idx]
    return total


# -1 - 0 = index -1 = (3) // -1 -1 = index -2 = (5) // -1 - 2 = index -3 (7) //


# print(L[i][-1 - i])....-1 = the last element of the nested list.
# Therefore -1 at each index equals 3, 6, and 9.
# When you subtract the -1 index (3,6,9) by the index of the nested list (0,1,2)
# You get 3-0 = 3 // 6-1 = 5 // 9-2 = 7
