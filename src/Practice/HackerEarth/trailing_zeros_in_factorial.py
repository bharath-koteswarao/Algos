# from math import factorial as fact
#
#
# def zeros(num):
#     i = -1
#     count = 0
#     while num[i] == '0':
#         count += 1
#         i -= 1
#     return count
#
#
# if __name__ == '__main__':
#     for i in range(0, 1001):
#         a = fact(i)
#         print(i, zeros(str(a)))


def skip(n):
    count = 0
    i = 1
    while True:
        if n // (5 ** i) == 0:
            break
        else:
            count += ((n // (5 ** i)) - 1)
            i += 1
    return count


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        n = int(input())
        start = (n - skip(n)) * 5
        print(5)
        print(start, start + 1, start + 2, start + 3, start + 4)
