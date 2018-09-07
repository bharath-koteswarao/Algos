def check(n, x, k):
    if n * x < k:
        return False
    else:
        return True


if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    # h = 1
    # while n * h < k:
    #     h += 1
    # print(h)
    start, end = 1, k
    mid = (start + end) // 2
    while start <= end:
        if check(n, mid, k):
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2
    print(start)

# mid = (self.start + self.end) // 2
# while self.start <= self.end:
#     if self.check(mid):
#         self.start = mid + 1
#     else:
#         self.end = mid - 1
#     mid = (self.start + self.end) // 2
# return self.start if self.check(self.start) else self.start - 1
