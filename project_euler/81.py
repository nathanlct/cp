def solve(s):
    matrix = list(map(lambda s: list(map(int, s.split(','))), s.split('\n')))
    matrix = [[1e15] * len(matrix[0])] + matrix  # pad first row
    matrix = [[1e15] + row for row in matrix]  # pad first column
    matrix[1][0] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            matrix[row][col] += min(matrix[row][col - 1], matrix[row - 1][col])
    
    return matrix[-1][-1]


# solve

s0 = """131,673,234,103,18
201,96,342,965,150
630,803,746,422,111
537,699,497,121,956
805,732,524,37,331"""

with open('81_matrix.txt', 'r') as fp:
    s1 = fp.read()

print(solve(s0))
print(solve(s1))