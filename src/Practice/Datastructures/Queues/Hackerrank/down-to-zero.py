import math

n = int(input())


def construct_list(number):
    if number is 0:
        return 0
    elif number is 1:
        return 1
    else:
        for i in range(math.ceil(math.sqrt(number)), 1, -1):
            if number % i == 0:
                return max(i, number % i)
        return -1


for i in range(0, n):
    l = [0, 1]
    num = int(input())
    for j in range(2, num + 1):
        maxx = construct_list(j)
        if maxx is -1:
            l.append(1 + l[j - 1])
        else:
            l.append(1 + min(maxx, l[j - 1]))
    print(l[num])
