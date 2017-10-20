if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    total, size = [int(i) for i in input().strip().split(" ")]
    prefix_sum = [arr[0]]
    for i in range(1, len(arr)):
        prefix_sum.append(arr[i] + prefix_sum[i - 1])
    # print(prefix_sum)
    start = -1
    count = 0
    for i in range(size - 1, len(prefix_sum)):
        if start >= 0:
            if prefix_sum[i] - prefix_sum[start] == total:
                count += 1
        else:
            if prefix_sum[i] == total:
                count += 1
        start += 1
    print(count)
