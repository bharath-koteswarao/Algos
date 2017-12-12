from decimal import Decimal as d


def terminates(n):
    dic = {}
    while n % 2 == 0 and n != 0:
        n //= 2
        dic[2] = 0
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0 and n != 0:
            n //= i
            dic[i] = 0
    if n > 2:
        dic[n] = 0
    if len(dic) > 2:
        return False
    elif len(dic) == 2:
        if 5 in dic and 2 in dic:
            return True
        else:
            return False
    elif len(dic) == 1:
        if 5 in dic or 2 in dic:
            return True
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    a, b, c = [int(i) for i in input().strip().split(" ")]
    if terminates(b):
        if a % b == 0:
            if c != 0:
                print(-1)
            else:
                print(1)
        else:
            p = a - (a // b) * b
            fr = str(p / b)[2:] + str(0)
            found = False
            for i in range(len(fr)):
                if fr[i] == str(c):
                    found = True
                    print(i + 1)
            if not found:
                print(-1)
        pass
    else:
        p = a - b * (a // b)
        if 'e' not in str(p / b):
            fr = p / b
            a = str(fr)[2:]
            found = False
            for i in range(len(a)):
                if a[i] == str(c):
                    print(i + 1)
                    found = True
                    break
            if not found:
                print(-1)
            pass
        else:
            fr = d(p) / d(b)
            a = str(fr)[2:]
            found = False
            for i in range(len(a)):
                if a[i] == str(c):
                    print(i + 1)
                    found = True
                    break
            if not found:
                print(-1)
