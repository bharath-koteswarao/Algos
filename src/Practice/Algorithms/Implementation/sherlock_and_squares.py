if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        a, b = [int(i) for i in input().strip().split(' ')]
        ans = (int(b ** 0.5) - int(a ** 0.5))
        if int(a ** 0.5) == a ** 0.5:
            ans += 1
        print(ans)
