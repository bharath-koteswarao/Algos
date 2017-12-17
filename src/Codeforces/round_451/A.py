if __name__ == '__main__':
    a = int(input().strip())
    re = a % 10
    if a == re:
        print(0)
    else:
        a -= re
        if re > 5:
            a += 10
        print(a)
