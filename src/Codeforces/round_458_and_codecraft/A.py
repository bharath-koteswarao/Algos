def ps(n):
    return n ** 0.5 == int(n ** 0.5)


if __name__ == '__main__':
    n = int(input().strip())
    ar = [int(i) for i in input().strip().split()]
    ar.sort(reverse=True)
    for i in ar:
        if i < 0 or not ps(i):
            print(i)
            break
