with open('42.txt', 'r') as fp:
    words = fp.read()

words = list(map(lambda s: s[1:-1], words.split(',')))

words_values = []
for word in words:
    words_values.append(0)
    for c in word:
        words_values[-1] += ord(c) - ord('A') + 1

triangle_numbers = [1]
n = 2
while triangle_numbers[-1] < max(words_values):
    triangle_numbers.append(n * (n + 1) // 2)
    n += 1

ans = 0
for val in words_values:
    if val in triangle_numbers:
        ans += 1
print(ans)
