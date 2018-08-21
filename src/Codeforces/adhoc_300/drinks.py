if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ans = 0
    for i in arr:
        ans += (i / 100)
    ans = ans / n
    print(ans * 100)