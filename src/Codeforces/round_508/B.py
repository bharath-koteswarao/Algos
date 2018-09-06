if __name__ == '__main__':
    n = int(input().strip())
    if n <= 2:
        print("No")
    else:
        print("Yes")
        s1, s2 = [], []
        for i in range(1, n + 1):
            if i % 2 == 0:
                s1.append(i)
            else:
                s2.append(i)
        print(len(s1), *s1)
        print(len(s2), *s2)
