if __name__ == '__main__':
    n = int(input().strip())
    a1 = [int(__) for __ in input().strip().split()]
    a2 = [int(__) for __ in input().strip().split()]
    no = "NIE"
    yes = "TAK"
    s1, s2 = sum(a1), sum(a2)
    if abs(s1 - s2) % 6 != 0:
        print(no)
    else:
        times = abs(s1 - s2) / 6
