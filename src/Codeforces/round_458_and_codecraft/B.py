from bisect import bisect_left as bs
from collections import Counter


def get(ar):
    c = Counter(ar)
    m = ar[-1]
    if c[m] == len(ar):
        return "Conan" if c[m] % 2 == 1 else "Agasa"
    elif c[m] % 2 == 1:
        return "Conan"
    else:
        ind = bs(ar, m - 0.1)
        return get(ar[:ind])


if __name__ == '__main__':
    n = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    ar.sort()
    ans = get(ar)
    print(ans)
