def getAns(idx, ans):
    if idx == n:
        return ans
    else:
        breakNext = False
        mi = float('inf')
        while idx < n and not breakNext:
            breakNext = heights[idx] < heights[idx + 1]
            mi = min(mi,
                     getAns(idx + 1, ans + (0 if idx + 1 == n else abs(heights[idx + 1] - heights[idx])) + prices[idx]))
            idx += 1
        return mi


if __name__ == '__main__':
    n = int(input().strip())
    mas = int(input().strip())
    heights = [mas] + [int(_) for _ in input().strip().split()] + [0]
    prices = [0] + [int(_) for _ in input().strip().split()] + [0]
    ans = getAns(0, 0)
    print(ans)
