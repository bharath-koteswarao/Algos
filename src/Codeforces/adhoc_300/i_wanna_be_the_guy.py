if __name__ == '__main__':
    n = int(input().strip())
    a1 = [int(__) for __ in input().strip().split()][1:]
    a2 = [int(__) for __ in input().strip().split()][1:]
    a = (list(set(a1 + a2)))
    print("I become the guy." if len(a) == n else "Oh, my keyboard!")
