from collections import Counter as c
from math import factorial as f

if __name__ == '__main__':
    s = input().strip()
    for _ in range(int(input().strip())):
        l, r = [int(i) for i in input().strip().split()]
        l, r = l - 1, r
        count = c(s[l:r])
        e, o, r = 0, 0, 1
        for i in count:
            t = count[i] // 2
            if count[i] % 2 == 0:
                e += t
                r *= f(t - 1) if t > 1 else 1
            else:
                o += 1
                e += t
                r *= f(t - 1) if t > 1 else 1
        o = o if o != 0 else 1
        print((o * f(e)) // r)
