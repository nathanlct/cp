memoiz = {}

def collatz_length(N):
    if N == 1: return 1
    if N in memoiz: return memoiz[N]

    next_N = N // 2 if N % 2 == 0 else 3 * N + 1
    length = 1 + collatz_length(next_N)
    memoiz[N] = length
    return length

max_length = 0
argmax_length = 0
for i in range(1, int(1e6)):
    length = collatz_length(i)
    if length > max_length:
        max_length = length
        argmax_length = i
print(argmax_length)