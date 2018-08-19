if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        su = 0
        for i in range(n):
            if i % 2 == 0:
                if su >= 0:
                    su += arr[i]
                else:
                    su -= arr[i]
            else:
                # miksi
                if su >= 0:
                    su -= arr[i]
                else:
                    su += arr[i]
        print(1 if abs(su) >= k else 2)
