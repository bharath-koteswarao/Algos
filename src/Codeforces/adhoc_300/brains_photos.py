def find(l):
    for x in l:
        if len({'C', 'M', 'Y'}.intersection(set(x))) > 0:
            return True
    return False


if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    l = []
    for _ in range(n):
        l.append(input().strip().split())
    res = find(l)
    print("#Color" if res else "#Black&White")
