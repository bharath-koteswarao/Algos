from collections import Counter

if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    for _ in range(int(input().strip())):
        l, r = [int(__) for __ in input().strip().split()]
        l, r = l - 1, r - 1
        ans = 0
        c = Counter(arr[l:r + 1])
        for i in c:
            if c[i] == 1:
                ans += 1
        print(ans)
