# from math import sqrt
#
#
# def two_point_distance(x1, y1, x2, y2):
#     return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
#
#
# if __name__ == '__main__':
#     n, q = [int(__) for __ in input().strip().split()]
#     circles = []
#     for _ in range(n):
#         x, y, r = [int(__) for __ in input().strip().split()]
#         circles.append((x, y, r))
#
#     for _ in range(q):
#         k = int(input().strip())
#         ans = 0
#         for i in range(len(circles)):
#             for j in range(i + 1, len(circles)):
#                 x1, y1, r1 = circles[i]
#                 x2, y2, r2 = circles[j]
#                 c1c2 = two_point_distance(x1, y1, x2, y2)
#                 if c1c2 >= r1 + r2:
#                     # Circles are outside
#                     dist = abs(c1c2 - r1 - r2)
#                     ans += 1 if dist <= k else 0
#                     pass
#                 else:
#                     if abs(r1 - r2) == c1c2:
#                         # Circles touch internally
#                         ans += 1
#                     elif c1c2 < abs(r1 - r2):
#                         if r1 > r2:
#                             ans += 1 if abs(c1c2 + r2 - r1) <= k else 0
#                             pass
#                         else:
#                             ans += 1 if abs(c1c2 + r1 - r2) <= k else 0
#                     else:
#                         # Circles intersect
#                         ans += 1
#         print(ans)

fig = "G:\\bk.jpg"