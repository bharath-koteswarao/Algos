#!/bin/python3


t = int(input().strip())


def calculate(n):
    # n = int(input().strip())
    is_set = False
    answer = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            k = n - i - j
            if i + j + k == n and i ** 2 + j ** 2 == k ** 2:
                answer = max(answer, i * j * k)
                if answer == 1620:
                    print(i,j,k)
                is_set = True
    if not is_set:
        print(n, -1)
    else:
        print(n, answer)


for a0 in range(1, t + 1):
    calculate(a0)
