if __name__ == '__main__':
    tc = int(input().strip())
    test_cases = []
    for i_tc in range(tc):
        test_cases.append(int(input().strip()))
    largest = max(test_cases)
    memo = {}
    f1 = 1
    f2 = 1
    count = 2
    while len(str(f2)) < largest:
        temp = f2
        f2 += f1
        f1 = temp
        count += 1
        if len(str(f2)) not in memo:
            memo[len(str(f2))] = count
    for test_case in test_cases:
        print(memo[test_case])
