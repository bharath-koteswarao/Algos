def getAns(i, j, ans):
    if j == n:
        return ans
    else:
        l = []
        mi = float('inf')
        while movingCost[i][j] != -1 and j < n:
            mi = min(mi,getAns(i,j,ans+movingCost[j][j + 1]))
            j += 1
        return min(l)


if __name__ == '__main__':
    n = int(input().strip())
    mas = int(input().strip())
    heights = [mas] + [int(_) for _ in input().strip().split()] + [0]
    prices = [0] + [int(_) for _ in input().strip().split()] + [0]
    movingCost = [[-1 for _ in range(n + 1)] for __ in range(n + 1)]
    for i in range(n + 1):
        breakNext = False
        for j in range(i + 1, n + 1):
            if breakNext:
                break
            else:
                breakNext = heights[j] > heights[i]
                cost = prices[j] + (float('inf') if j == n else abs(heights[i] - heights[j]))
                movingCost[i][j] = cost
    movingCost[0][0] = 0
    for i in movingCost:
        for j in i:
            print(j, end=" ")
        print()
    ans = getAns(0, 0, 0)
    print(ans)
