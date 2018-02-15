if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0:
        arr = ['8'] * (n // 2)
    else:
        arr = ['0'] * n
    print(''.join(arr))