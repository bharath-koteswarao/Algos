if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    r = True
    for _ in range(n):
        if _ % 2 == 0:
            print('#' * m)
        else:
            print('.' * (m - 1) + '#' if r else '#' + '.' * (m - 1))
            r = not r
