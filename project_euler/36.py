# or bin()
from math import log2
def int2bin(n):
    if n == 0: 
        return '0'

    b = ''
    pwr = 2 ** int(log2(n))
    while pwr > 0:
        if pwr <= n:
            n -= pwr
            b += '1'
        else:
            b += '0'
        pwr //= 2
    return b

def is_palindrome(s):
    if len(s) == 1: 
        return True
    mid = len(s) // 2
    return s[mid:] == s[:-mid][::-1]

ans = 0
for i in range(int(1e6)):
    if is_palindrome(str(i)) and is_palindrome(int2bin(i)):
        ans += i
print(ans)