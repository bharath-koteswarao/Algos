if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        input()
        arr = [int(i) for i in input().strip().split(" ")]
        prefix_sum = [0]
        suffix_sum = [0 for i in range(len(arr))]
        for i in range(1, len(arr)):
            prefix_sum.append(prefix_sum[i - 1] + arr[i - 1])
        for i in range(len(arr) - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + arr[i + 1]
        possible = False
        for i in range(len(arr)):
            if prefix_sum[i] == suffix_sum[i]:
                possible = True
                break
        print("YES" if possible else "NO")
