if __name__ == '__main__':
    k, p = [int(i) for i in input().strip().split(" ")]
    s = 0
    for i in range(1, k + 1):
        s += int(str(i) + str(''.join(list(reversed(str(i))))))
    print(s % p)
