from math import sqrt


def two_point_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def lies_between(current_circle, small_circle, big_circle):
    center = (small_circle[0], small_circle[1])
    radius_small = small_circle[2]
    radius_big = big_circle[2]
    dist = two_point_distance(center[0], center[1], current_circle[0], current_circle[1])
    nd = dist - current_circle[2]
    fd = dist + current_circle[2]
    if nd <= radius_small and fd >= radius_big:
        return True
    elif radius_small <= nd <= radius_big:
        return True
    elif nd <= radius_small <= fd <= radius_big:
        return True
    else:
        return False


if __name__ == '__main__':
    n, q = [int(__) for __ in input().strip().split()]
    circles = []
    for _ in range(n):
        x, y, r = [int(__) for __ in input().strip().split()]
        circles.append((x, y, r))

    for _ in range(q):
        k = int(input().strip())
        ans = 0
        for i in range(len(circles)):
            for j in range(i + 1, len(circles)):
                x1, y1, r1 = circles[i]
                x2, y2, r2 = circles[j]
                c1c2 = two_point_distance(x1, y1, x2, y2)
                small_circle = (x1, y1, abs(r1 - k))
                big_circle = (x1, y1, r1 + k)
                current_circle = circles[j]
                if lies_between(current_circle, small_circle, big_circle):
                    ans += 1
                # if c1c2 >= r1 + r2:
                #     # Outside
                #     small_circle = (x1, y1, abs(r1 - k))
                #     big_circle = (x1, y1, r1 + k)
                #     current_circle = circles[j]
                #     if lies_between(current_circle, small_circle, big_circle):
                #         ans += 1
                # else:
                #     # Inside
                #
                #     pass
        print(ans)