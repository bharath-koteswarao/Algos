def isC(n):
    co = 0
    while n % 2 == 0 and n != 0:
        n //= 2
        co += 1
    if co >= 3:
        return True
    for i in range(3, int(n ** 0.5) + 1, 2):
        co = 0
        while n % i == 0 and n != 0:
            n //= i
            co += 1
        if co >= 3:
            return True
    return False


if __name__ == '__main__':
    l = [0 for i in range(1000)]
    for i in range(2, 999):
        l[i] = i ** 3
    