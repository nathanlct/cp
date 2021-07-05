# same as pb 18

with open('67_triangle.txt', 'r') as fp:
    triangle = fp.read()

def max_column(s):
    pyramid = [
        [0] + list(map(int, row.split(' '))) + [0]  # padding
        for row in s.split('\n')[:-1]
    ]

    # add from top to bottom
    for row in range(1, len(pyramid)):
        for col in range(1, len(pyramid[row]) - 1):  # mind padding
            pyramid[row][col] += max(pyramid[row-1][col], pyramid[row-1][col-1])
    
    return max(pyramid[-1])

print(max_column(triangle))
