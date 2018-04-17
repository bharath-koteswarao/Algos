from math import ceil


def roundUp(n, d=2):
    d = int('1' + ('0' * d))
    return ceil(n * d) / d


if __name__ == '__main__':
    su, co = 0, 0
    for _ in range(int(input().strip())):
        cur = int(input().strip())
        if cur >= 90:
            su += cur
            co += 1
    if co == 0:
        print("0.00")
    else:
        r1 = round(su / co, 3)
        print(roundUp(r1))
