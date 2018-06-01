from heapq import *


def heapify_node(idx, arr):
    pass


def my_heapify(arr):
    last_parent = (len(arr) // 2) - 1
    for i in range(last_parent, -1, -1):
        heapify_node(i, arr)
    pass


if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    heapify(arr)
    ans = 0
    valid = True
    while arr[0] < k:
        if len(arr) < 2:
            valid = False
            break
        ans += 1
        x = heappop(arr)
        y = heappop(arr)
        heappush(arr, x + 2 * y)
    print(ans if valid else -1)
