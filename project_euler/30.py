"""
let n be a number that can be written as a sum of its digits at the Nth power
then n is at most n_digits(n) * 9^N
"""


def solve(N):
    ans = 0
    i = 2
    max_digit = 9 ** N
    while True:
        sum_powers = sum([int(digit) ** N for digit in list(str(i))])
        if sum_powers == i:
            ans += i
        if len(str(len(str(i)) * max_digit)) < len(str(i)):
            break
        i += 1
    return ans


print(solve(4))
print(solve(5))