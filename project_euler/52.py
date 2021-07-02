"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

n = 13
while True:
    n += 1

    # first digit has to be 1 so that 6x has the same nb of digits
    if str(n)[0] != '1': 
        continue

    candidate = True
    digits = set(list(str(n)))
    for k in [2, 3, 4, 5, 6]:
        if digits != set(list(str(k * n))):
            candidate = False
            break

    if candidate:
        print(n)
        break
