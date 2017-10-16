def is_prime(n):
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    tc = int(input().strip())
    lowar = []
    upper = []
    test_cases = []
    dic = {}
    for i_tc in range(tc):
        l, u = [int(i) for i in input().strip().split(" ")]
        test_cases.append((l, u))
        lowar.append(l)
        upper.append(u)
    for i in range(min(lowar), max(upper) + 1):
        if is_prime(i) and i != 1:
            dic[i] = i
    for (l, u) in test_cases:
        while l != u + 1:
            if l in dic:
                print(l)
            l += 1
        print()
