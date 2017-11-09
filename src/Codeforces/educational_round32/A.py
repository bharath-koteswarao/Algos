if __name__ == '__main__':
    input()
    inp = [int(i) for i in input().strip().split(" ")]
    count = 0
    if len(inp) <= 1:
        print(0)
    elif len(inp) == 2:
        print(2)
    else:
        for i in range(1, len(inp) - 1):
            if inp[i] > inp[i - 1] and inp[i] > inp[i + 1]:
                count += 1
            elif inp[i] < inp[i - 1] and inp[i] < inp[i + 1]:
                count += 1
        print(count)
