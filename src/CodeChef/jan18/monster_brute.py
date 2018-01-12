def get(s, i, l, ans):
    if i != len(s):
        if s[i] == '1':
            get(s, i + 1, l, ans + '1')
            get(s, i + 1, l, ans + '0')
        else:
            get(s, i + 1, l, ans + '0')
    else:
        l.append(int(ans, 2))


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    alive = n
    for _ in range(int(input().strip())):
        x, y = [int(i) for i in input().strip().split()]
        l = []
        get(bin(x)[2:], 0, l, "")
        for i in l:
            if i < n and arr[i] > 0:
                arr[i] -= y
                if arr[i] <= 0:
                    alive -= 1
        print(alive)
