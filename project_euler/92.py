def solve1():
    squares = { str(d): d * d for d in range(10) }

    memoiz = { 1: 1, 89: 89 }
    def get_final_number(n):
        if n not in memoiz:
            memoiz[n] = get_final_number(sum([squares[digit] for digit in str(n)]))
        return memoiz[n]

    print(get_final_number(44))
    print(get_final_number(85))

    ans = 0
    for i in range(1, int(1e7)):
        if get_final_number(i) == 89:
            ans += 1
            print(i)
    print('ans', ans)

def solve2():
    # try something faster
    # since permutations of the same number should return the same result, we can only consider numbers
    # with non-decreasing digits from left to right

    squares = [digit * digit for digit in range(10)]
    finals = { 0: 0 }
    for n in range(1, 7 * 9 * 9 + 1):  # after one application of the operation, the number becomes 7*9^2 at most
        x = n
        while x != 1 and x != 89:
            x = sum([int(d) ** 2 for d in str(x)])
        finals[n] = x

    def gen_digits(depth_left=6, min_digit=0):
        for digit in range(min_digit, 10):
            sq = squares[digit]
            if depth_left == 0:
                yield [sq]
            else:
                for digits_left in gen_digits(depth_left=depth_left-1, min_digit=digit):
                    yield [sq] + digits_left
    
    ans = 0
    for x in gen_digits():
        final = finals[sum(x)]
        if final == 89:
            # count number of permutations (n! for an n-digit number)
            n_permutations = 1
            for k in range(2, len(x) + 1):
                n_permutations *= k
            # if there are k times the same digits in the permutation, divide n_permutations by k! to discard order
            for val in set(x):
                for k in range(2, x.count(val) + 1):
                    n_permutations //= k
            ans += n_permutations
    print(ans)

solve2()

