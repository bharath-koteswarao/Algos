if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        n = int(input().strip())
        inp = [int(i) for i in input().strip().split(" ")]
        prefix_sum = [inp[0]]
        for i in range(1, len(inp)):
            prefix_sum.append(inp[i] + prefix_sum[i - 1])
        non_contiguous = 0
        for i in range(n):
            non_contiguous += inp[i] if inp[i] > 0 else 0
        if non_contiguous == 0:
            non_contiguous = max(inp)
            contiguous = non_contiguous
        else:
            positive_max = contiguous = inp[0]
            for i in range(1, n):
                positive_max += inp[i]
                if positive_max < 0:
                    positive_max = 0
                contiguous = max(positive_max, contiguous)
        print(contiguous, non_contiguous)
