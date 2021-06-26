# sum_{k=1}^{N//a} a*k = a (N//a)(N//a + 1)/2
sum_a = lambda a, N: a * (N // a) * (N // a + 1) // 2
ans = lambda N: sum_a(3, N-1) + sum_a(5, N-1) - sum_a(15, N-1)

print(ans(10))
print(ans(1000))