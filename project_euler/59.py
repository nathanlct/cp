with open('59_cipher.txt', 'r') as fp:
    encoded = list(map(int, fp.read().split(',')))

alphabet = [ord('a') + k for k in range(26)]
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            out = list(encoded)
            for i in range(0, len(encoded), 3): out[i] ^= a
            for i in range(1, len(encoded), 3): out[i] ^= b
            for i in range(2, len(encoded), 3): out[i] ^= c
            out = ''.join(list(map(chr, out)))
            if ' the ' in out:
                print(sum([ord(c) for c in out]), out)