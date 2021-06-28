# 7-digit numbers at most
# since 8 * 9! has 7 digits and the difference grows

facts = [1, 1]
for i in range(2, 10):
    facts.append(facts[-1] * i)

# brute force ;_;
ans = 0
for i in range(3, int(1e7)):
    s = sum([facts[digit] for digit in map(int, list(str(i)))])
    if s == i:
        print(s)
        ans += s
print(ans)