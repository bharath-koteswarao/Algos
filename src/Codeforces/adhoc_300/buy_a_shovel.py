if __name__ == '__main__':
    k, r = [int(__) for __ in input().strip().split()]
    ans = 1
    while True:
        cal = ans * k
        if cal % 10 == 0 or cal % 10 == r:
            break
        else:
            ans += 1
    print(ans)