if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        x = n
        arr = [int(i) for i in input().strip().split()]
        arr = arr[::-1]
        i = 0
        while arr[i] == 0 and i < n:
            i += 1
            x -= 1
        if i == n - 1:
            print(0)
        else:
            ans = []
            if arr[i] > 0:
                ans.append(1)
            else:
                ans.append(-1)
            # neg sgn
            if n % 2 == 0:
                if arr[i] > 0:
                    ans.append(1)
                else:
                    ans.append(-1)
            else:
                if arr[i] < 0:
                    ans.append(1)
                else:
                    ans.append(-1)
            print(*ans)
