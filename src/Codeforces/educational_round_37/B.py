if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        ans = []
        c = 1
        for i in range(n):
            a, b = [int(i) for i in input().strip().split()]
            if c <= b:
                ans.append(c)
                c += 1
            else:
                ans.append(0)
        for i in ans:
            print(i, end=" ")
        print()
