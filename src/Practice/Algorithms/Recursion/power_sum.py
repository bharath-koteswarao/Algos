from math import floor

answer = 0


def calculate(total, lis, find, lengths):
    print(total,lis,find,lengths)
    global answer
    if total is find:
        # print(total, lis, find)
        lengths.append(len(lis))
        answer += 1
        pass
    elif len(lis) in lengths:
        pass
    elif len(lis) is 0:
        pass
    elif total > find:
        pass
    else:
        for i in lis:
            tmp = lis[:]
            tmp.remove(i)
            calculate(total + i, tmp, find, lengths)


if __name__ == '__main__':
    number = int(input())
    power = int(input())
    l = []
    for i in range(1, floor(number ** float(1 / power)) + 1):
        l.append(i ** power)
    lengths = []
    calculate(0, l, number, lengths)
    print(len(set(lengths)))
