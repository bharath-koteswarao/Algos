if __name__ == '__main__':
    input()
    inp = [int(i) for i in input().strip().split(" ")]
    first, second = 0, 0
    inp = sorted(inp)[::-1]
    for i in inp:
        if first <= second:
            first += i
        else:
            second += i
    print(abs(first - second))
