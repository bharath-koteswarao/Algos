if __name__ == '__main__':
    su = 0
    for _ in range(int(input().strip())):
        c, n = input().strip().split()
        if c == "set":
            su = max(su, int(n))
        else:
            su = max(su, su + int(n))
    print(su)
