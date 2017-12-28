from collections import defaultdict as dfd

if __name__ == '__main__':
    n = int(input().strip())
    dic = dfd(list)
    arr = [int(i) for i in input().strip().split(" ")]
    for i in range(len(arr)):
        dic[arr[i]].append(i)
    ar = dic[min(arr)]
    mi = 10 ** 10
    for i in range(len(ar) - 1):
        mi = min(mi, ar[i + 1] - ar[i])
    print(mi)
