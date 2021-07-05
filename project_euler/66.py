"""
x^2 - D y^2 = 1
test all squares for x^2, then test if y^2 = (x^2 - 1) / D is a square
too slow

use Chakravala method (https://en.wikipedia.org/wiki/Chakravala_method)
"""

def find_x_y(D):

    # get one solution of x^2 - D * y^2 = k
    y = 1
    x = min([k for k in range(100) if k * k > D])
    k = x * x - y * D

    while k != 1:
        # find m > 0 such that (x + y * m) % k == 0, minimizing |m^2 - D|
        m = 0
        min_m = 1e20

        i = 1
        while i < 3 * (D ** 0.5):
            if (x + y * i) % k == 0:
                if (v := abs(i * i - D)) < min_m:
                    min_m = v
                    m = i
            i += 1
        if m == 0:
            while True:
                if (x + y * i) % k == 0:
                    m = i
                    break
                i += 1

        # compute new solution (https://en.wikipedia.org/wiki/Brahmagupta%27s_identity)
        x, y, k = (x * m + D * y) // abs(k), (x + y * m) // abs(k), (m * m - D) // k

    # we found a solution (proved to converge)
    return x, y


def solve(N):
    squares = [k * k for k in range(N + 1)]
    max_x = 0
    argmax_x = 0
    for D in range(2, N + 1):
        if D in squares:
            continue
        x, y = find_x_y(D)
        if x > max_x:
            max_x = x
            argmax_x = D
    return argmax_x

print(solve(5))
print(solve(1000))


# def solve(N):
#     max_x2 = 0
#     argmax_x2 = -1
#     for D in range(2, N + 1):
#         if D in squares_set:
#             continue
#         square_found = False
#         for x2 in squares[2:]:
#             if (x2 - 1) % D == 0 and (x2 - 1) // D in squares_set:
#                 square_found = True
#                 if x2 > max_x2:
#                     max_x2 = x2
#                     argmax_x2 = D
#                     print(f'D={D}, x2={x2}')
#                 break
#         if not square_found:
#             print('square not found for D =', D)
#     return argmax_x2

# print(solve(7))
# print(solve(1000))
