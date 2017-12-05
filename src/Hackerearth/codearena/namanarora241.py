def find_min(total, lis):
    if total == 0:
        return 0
    elif total < 0 or total < lis[0]:
        return float('inf')
    else:
        temp = []
        for i in lis:
            temp.append(1 + find_min(total-i,lis))
        print(min(temp))


if __name__ == '__main__':
    n, m = [int(i) for i in input().strip().split(" ")]
    i = 0
    lis = []
    if m == 1:
        print(n)
    else:
        while True:
            if m ** i > n:
                break
            else:
                lis.append(m ** i)
                i += 1
        ans = find_min(n, lis)
        print(ans)
