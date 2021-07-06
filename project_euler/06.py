sum_of_squares = lambda N: N * (N + 1) * (2 * N + 1) // 6
square_of_sum = lambda N: N * N * (N + 1) * (N + 1) // 4

print(square_of_sum(10) - sum_of_squares(10))
print(square_of_sum(100) - sum_of_squares(100))