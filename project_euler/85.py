def n_rectangles(w, h):
    total_count = 0
    for subw in range(1, w + 1):
        for subh in range(1, h + 1):
            countw = w - subw + 1
            counth = h - subh + 1
            total_count += countw * counth
    return total_count

def solve():
    nearest_diff = 1e15
    argmax_area = 0

    # go through all w < h
    h = 2
    while True:
        w = 1
        while w < h:
            count = n_rectangles(w, h)
            if (diff := abs(count - 2e6)) < nearest_diff:
                nearest_diff = diff
                argmax_area = w * h
            if count > 1e7:
                return argmax_area
            w += 1
        h += 1

print(solve())
