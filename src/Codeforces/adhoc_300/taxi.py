if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ans = 0
    ans += arr.count(4)

    ones = arr.count(1)
    two = arr.count(2)
    three = arr.count(3)

    ans += two // 2
    two = two % 2

    mi = min(three, ones)
    ans += mi
    three -= mi
    ones -= mi

    if two == 1:
        if ones != 0:
            if ones >= 2:
                two = 0
                ans += 1
                ones -= 2
            else:
                two = 0
                ans += 1
                ones = 0

    ans += three
    ans += ones // 4
    ones = ones % 4
    ans += 1 if ones > 0 else 0
    ans += 1 if two > 0 else 0
    print(ans)
