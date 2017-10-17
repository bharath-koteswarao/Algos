if __name__ == '__main__':
    factorial = {
        0: 1,
        1: 1,
        2: 2,
        3: 6,
        4: 24,
        5: 120,
        6: 720,
        7: 5040,
        8: 40320,
        9: 362880,
        10: 3628800,
        11: 39916800,
        12: 479001600,
        13: 6227020800, }
    tc = int(input().strip())
    for i_tc in range(tc):
        l = list('abcdefghijklm')
        n = int(input().strip()) - 1
        indices = [0 for i in range(len(l))]
        for i in range(len(l) - 1, -1, -1):
            indices[len(l) - i - 1] = n // factorial[i]
            n = n % factorial[i]
        # print(indices)
        for i in indices:
            print(l[i], end="")
            l.remove(l[i])
