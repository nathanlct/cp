digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', \
          'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dozens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def number2str(N):
    assert (N > 0 and N < 1e6)
    n_thousands = N // 1000
    N %= 1000
    n_hundreds = N // 100
    N %= 100
    n_dozens = N // 10
    if n_dozens == 1:
        n_dozens = 0
    else:
        N %= 10
    n_units = N

    s = ''
    if n_thousands > 0:
        s += f'{number2str(n_thousands)} thousand '
        if n_hundreds == 0 and (n_dozens > 0 or n_units > 0):
            s += 'and '
    if n_hundreds > 0:
        s += f'{number2str(n_hundreds)} hundred '
        if n_dozens > 0 or n_units > 0:
            s += 'and '
    if n_dozens > 0:
        s += f'{dozens[n_dozens]} '
    if n_units > 0:
        s += f'{digits[n_units]}'
    return s

ans = 0
for i in range(1, 1001):
    ans += len(number2str(i).replace(' ', ''))
print(ans)
