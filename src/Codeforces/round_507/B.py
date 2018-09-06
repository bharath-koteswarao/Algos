from math import ceil

if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    if k == 0:
        print(n)
        for i in range(n):
            print(i + 1, end=" ")
    else:
        if n <= 2 * k + 1:
            print(1)
            print(ceil(n / 2))
        else:
            l = []
            co = 0
            arr = [i + 1 for i in range(n)]
            while len(arr) > 0:
                if len(arr) > 2 * k + 1:
                    co += 1
                    l.append(arr[k])
                elif len(arr) == 2 * k + 1:
                    co += 1
                    l.append(arr[k])
                elif len(arr) <= 2 * k + 1:
                    break
                arr = arr[2 * k + 1:]
            if len(arr) > 0:
                if len(arr) <= k:
                    co += 1
                    for i in range(len(l)):
                        l[i] -= (k - len(arr) + 1)
                    l.append(arr[-1])
                else:
                    co += 1
                    l.append(arr[k])
            print(co)
            print(' '.join([str(i) for i in l]))
