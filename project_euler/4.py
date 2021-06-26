def largest_pal(N):
    max_pal = 0
    for i in range(N+1):
        for j in range(N+1):
            v = i * j
            v_str = str(v)
            l = len(v_str)
            if v_str[:l//2] == v_str[(l+1)//2:][::-1]:
                max_pal = max(max_pal, v)
    return max_pal

print(largest_pal(99))
print(largest_pal(999))