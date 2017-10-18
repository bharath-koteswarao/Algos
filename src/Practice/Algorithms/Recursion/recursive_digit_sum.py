def digit_sum(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s


def super_digit(n):
    if len(str(n)) == 1:
        return n
    else:
        return super_digit(digit_sum(n))


if __name__ == '__main__':
    n, k = input().strip().split(" ")
    k = int(k)
    temp = n
    for i in range(k):
        n += n
    ans = super_digit(int(n))
    print(ans)
