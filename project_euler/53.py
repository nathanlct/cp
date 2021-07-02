"""
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
In combinatorics, we use the notation C(3, 5) = 10.
In general, C(r, n) = n! / (r! (n - r)!) for r <= n.
It is not until n >= 23, that a value exceeds one-million: C(10, 23) = 1144066
How many, not necessarily distinct, values of C(r, n) for 1 <= n <= 100, are greater than one-million?
"""

fact_memoiz = { 0: 1 }
def fact(n):
    if n not in fact_memoiz:
        fact_memoiz[n] = n * fact(n - 1)
    return fact_memoiz[n]

def binomial(r, n):
    return fact(n) // (fact(r) * fact(n - r))

ans = 0

for n in range(1, 101):
    for r in range(n):
        if binomial(r, n) > 1e6:
            ans += 1

print(ans)