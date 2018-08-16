if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    print(max(
        a + b + c,
        (a + b) * c,
        a * (b + c),
        a * b * c,
        a * b + c,
        a + b * c
    ))
