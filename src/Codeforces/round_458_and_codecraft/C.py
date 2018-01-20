if __name__ == '__main__':
    mod = 1000000007
    dic = {}
    n = input().strip()
    k = int(input().strip())
    ones = n.count('1')
    s = '1' * ones + (len(n) - ones) * '0'
    dif = (int(s, 2) - int(n, 2)) % mod

