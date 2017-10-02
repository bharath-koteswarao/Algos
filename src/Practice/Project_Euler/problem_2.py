if __name__ == '__main__':
    tc = int(input().strip())
    for z0 in range(tc):
        n = int(input().strip())
        l = [1, 2]
        total = 2
        while l[-1] + l[-2] < n:
            total += l[-1] + l[-2] if (l[-1] + l[-2]) % 2 is 0 else 0
            l.append(l[-1] + l[-2])
        print(total,l)
