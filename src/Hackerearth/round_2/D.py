from collections import Counter

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(i) for i in input().strip().split()]
        c = Counter(arr)
        arr.sort()
        if len(set(arr)) == n:
            print(1)
        else:
            print(1 + n - len(set(arr)))
