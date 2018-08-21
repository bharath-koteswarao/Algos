if __name__ == '__main__':
    n = int(input().strip())
    ans = ""
    for i in range(n - 1):
        if i % 2 == 0:
            ans += "I hate that "
        else:
            ans += "I love that "
    if n % 2 == 0:
        ans += "I love it"
    else:
        ans += "I hate it"
    print(ans.strip())