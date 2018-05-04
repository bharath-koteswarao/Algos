if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        a = [int(__) for __ in input().strip().split()]
        xor = a[0] * 2
        for i in range(1, n):
            xor ^= (a[i] * 2)
        print(xor)
