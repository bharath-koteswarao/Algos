"""
6
1 2 5 3 4 6
01110
"""


def sort_this_part(start, end):
    so = sorted(arr)
    arr[start:end + 1] = so[start:end + 1]


if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    l = list(input().strip()) + ['0']
    i = 0
    while i < n - 1:
        if l[i] == '1':
            start = i
            while l[i] == '1' and i < n - 1:
                i += 1
            i += 1
            sort_this_part(start, i)
        else:
            i += 1
    print("YES" if arr == sorted(arr) else "NO")
