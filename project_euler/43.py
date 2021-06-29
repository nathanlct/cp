if False:
    def gen_permutations(arr):
        if len(arr) == 1:
            yield arr
        for first_digit in arr: #sorted(arr):
            other_digits = [d for d in arr if d != first_digit]
            sub_permutations = gen_permutations(other_digits)
            for perm in sub_permutations:
                yield [first_digit] + perm

    N = 9
    ans = 0
    permutations = gen_permutations(list(range(0, N+1))[::-1])
    for i, perm in enumerate(permutations):
        perm_str = ''.join(map(str, perm))
        candidate = True
        for i, div in enumerate([17, 13, 11, 7, 5, 3, 2]):
            if int(perm_str[7-i:7-i+3]) % div != 0:
                candidate = False
                break
        if candidate:
            ans += int(perm_str)
            print(perm_str)

    print('=>', ans)

def int2str_pad(val, pad=3):
    s = str(val)
    if len(s) < pad:
        s = ('0' * (pad - len(s))) + s
    return s

# try a faster way
ans = 0
for d0 in range(10):
    for d123 in range(12, 1000, 2):
        d123_str = int2str_pad(d123)
        for d456 in range(14, 1000, 7):
            d456_str = int2str_pad(d456)
            if int(d123_str[1:] + d456_str[0]) % 3 != 0: continue
            if int(d123_str[2:] + d456_str[:2]) % 5 != 0: continue
            for d789 in range(17, 1000, 17):
                d789_str = int2str_pad(d789)
                if int(d456_str[1:] + d789_str[0]) % 11 != 0: continue
                if int(d456_str[2:] + d789_str[:2]) % 13 != 0: continue
                n = str(d0) + d123_str + d456_str + d789_str
                if set(list(n)) != set(list('0123456789')): continue
                print(n)
                ans += int(n)

print('=>', ans)