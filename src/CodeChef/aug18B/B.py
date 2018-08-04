if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        bi = bin(n)[2:]
        le = len(bi)
        count = bi.count('1')
        if n == 1:
            print(2)
        elif count == 1:
            print(1)
        elif count == 2:
            print(0)
        else:
            sub = list(bi[:])
            cc = count
            idx = le - 1
            while cc > 2:
                if sub[idx] == '1':
                    sub[idx] = '0'
                    cc -= 1
                idx -= 1
            add = list(bi[:])
            req = 0
            found = False
            for i in range(1, len(add)):
                if add[i] == '1':
                    req = i
                    found = True
                    break
            if req == 1:
                found = False
            else:
                req -= 1
            if not found:
                add = bin(int('1' * len(add), 2) + 2)[2:]
            else:
                add = add[:req] + list('1' + '0' * (le - req - 1))
            # print(bin(n)[2:], n)
            # print(''.join(add), int(''.join(add), 2))
            # print(''.join(sub), int(''.join(sub), 2))
            print(min(
                int(''.join(add), 2) - n,
                n - int(''.join(sub), 2)
            ))
