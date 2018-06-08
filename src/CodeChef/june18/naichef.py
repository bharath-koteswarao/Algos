from collections import Counter as co

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, a, b = [int(__) for __ in input().strip().split()]
        count = co([int(__) for __ in input().strip().split()])
        ans = round((count[a] * count[b]) / (n ** 2), 10)
        print(ans)
