pentagonals = [1]
pentagonals_set = set(pentagonals)  # add set for checking if elt is pentagonal
# (goes from 1min to 1s compared to checking within list)
n = 2
while True:
    pent1 = n * (3*n - 1) // 2
    for pent0 in reversed(pentagonals[:n-1]):
        if pent1 - pent0 in pentagonals_set:
            s = pent0 + pent1
            m = len(pentagonals) + 1
            while max(pentagonals_set) < s:
                pentagonals.append(m * (3*m - 1) // 2)
                pentagonals_set.add(m * (3*m - 1) // 2)
                m += 1
            if s in pentagonals_set:
                print(abs(pent0 - pent1))
                import sys; sys.exit(0)
    if len(pentagonals) == n - 1:
        pentagonals.append(pent1)
        pentagonals_set.add(pent1)
    n += 1
