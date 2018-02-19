def dist(x1, y1, x2, y2):
    return abs(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


if __name__ == '__main__':
    r, x1, y1, p, q = [int(__) for __ in input().strip().split()]
    di = dist(x1, y1, p, q)
    if di >= r:
        print(x1, y1, r)
    else:
        xc1 = x1 + r * (((x1 - p) / (x1 - p) ** 2 + (y1 - q) ** 2) ** 0.5)
        xc2 = x1 - r * (((x1 - p) / (x1 - p) ** 2 + (y1 - q) ** 2) ** 0.5)
        a1 = r ** 2 - (xc1 - x1) ** 2
        a2 = r ** 2 - (xc2 - x1) ** 2
        if a1 > 0:
            yc1 = y1 + (r ** 2 - a1 ** 2) ** 0.5
            yc2 = y1 - (r ** 2 - a1 ** 2) ** 0.5
            dis1 = dist(xc1, yc1, p, q)
            dis2 = dist(xc2, yc2, p, q)
        else:
            yc1 = y1 + (r ** 2 - a2 ** 2) ** 0.5
            yc2 = y1 - (r ** 2 - a2 ** 2) ** 0.5
