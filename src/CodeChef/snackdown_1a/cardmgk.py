from bisect import bisect_right as bs
from collections import Counter

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        srtd = sorted(arr)
        co = Counter(arr)
        if arr == srtd:
            print("YES")
        else:
            idx = bs(srtd, arr[0])
            con_count = 0
            ch = arr[0]
            i = 0
            while arr[i] == ch:
                con_count += 1
                i += 1
            # print(srtd[idx:] + srtd[:idx])
            idx -= con_count
            # print(srtd[idx:] + srtd[:idx])
            if arr == srtd[idx:] + srtd[:idx]:
                print("YES")
            else:
                print("NO")
