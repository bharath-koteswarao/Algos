def n_ary(n, base):
    st = ""
    while n >= base:
        st += str(n % base)
        n //= base
    st += str(n)
    return st[::-1]


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    if sum(arr) % 3 != 0:
        print(0)
    else:
        l = []
        ans = 0
        for i in range(3 ** (n - 1)):
            s1, s2, s3 = [], [], []
            st = n_ary(i, 3)
            st = "0" * (n - len(st)) + st
            for x in range(len(st)):
                if st[x] == '0':
                    s1.append(arr[x])
                elif st[x] == '1':
                    s2.append(arr[x])
                else:
                    s3.append(arr[x])
            if sum(s1) == sum(s2) == sum(s3):
                ans += 3
                # l = [s1, s2, s3]
        print(ans)
