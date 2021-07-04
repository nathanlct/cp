def polygonal_number(s, n):
    return (s - 2) * n * (n - 1) // 2 + n

def solve(sides):
    # build all candidate polygonal numbers
    poly_numbers = {}
    for side in sides:
        poly_numbers[side] = []
        n = 0
        while (x := polygonal_number(side, n)) < 10000:
            if x >= 1000 and str(x)[2] != '0':
                poly_numbers[side].append(str(x))
            n += 1

    # build list of ([current cycle using n cycles], [the (len(sides) - n) sides left])
    paths = [([x], sides[1:]) for x in poly_numbers[sides[0]]]

    for _ in range(len(sides) - 1):
        new_paths = []
        for path, sides_left in paths:
            for side in sides_left:
                for val in poly_numbers[side]:
                    if path[-1][2:] == val[:2]:
                        new_paths.append(
                            (path + [val], [s for s in sides_left if s != side])
                        )
        paths = new_paths

    # end the cycle
    paths = [path[0] for path in paths if path[0][0][:2] == path[0][-1][2:]]
    return paths


s1 = solve([3, 4, 5])
print(s1)
s2 = solve([3, 4, 5, 6, 7, 8])
print(s2)
print(sum(map(int, s2[0])))