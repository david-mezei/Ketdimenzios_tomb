matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9, 10, 12]
]

# for sor in matrix:
#     for oszlop in sor:
#         print(oszlop, end=" ")
#     print()

for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], end=' ')