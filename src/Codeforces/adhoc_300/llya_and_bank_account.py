if __name__ == '__main__':
    n = input().strip()
    arr = [n, n[:-1], n[:-2] + n[-1]]
    print(max([int(i) for i in arr]))