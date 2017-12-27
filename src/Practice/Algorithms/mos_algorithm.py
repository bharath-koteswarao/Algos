"""
10
1 2 3 4 5 6 7 8 9 10
5
8 9
0 8
1 4
0 6
2 5
"""
if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    q = int(input().strip())
    answers = {}
    queries = []
    for i in range(q):
        l, r = [int(j) for j in input().strip().split(" ")]
        queries.append((l, r, i))
    queries.sort(key=lambda tup: (tup[0], tup[1]))
    print(queries)
    curL, curR, curSum = 0, 0, arr[0]
    for query in queries:
        l, r = query[0], query[1]
        while curL > l:
            curL -= 1
            curSum += arr[curL]
        while curL < l:
            curSum -= arr[curL]
            curL += 1
        while curR > r:
            curSum -= arr[curR]
            curR -= 1
        while curR < r:
            curR += 1
            curSum += arr[curR]
        answers[query[2]] = curSum
    print(answers)


    # while curL < l:
    #     curSum -= arr[curL]
    #     curL += 1
    # while curL > l:
    #     curSum += arr[curL - 1]
    #     curL -= 1
    # while curR <= r:
    #     curSum += arr[curR]
    #     curR += 1
    # while curR > r + 1:
    #     curSum -= arr[curR - 1]
    #     curR -= 1
