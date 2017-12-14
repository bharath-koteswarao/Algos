from math import factorial as fa

if __name__ == '__main__':
    n, q = [int(i) for i in input().strip().split(" ")]
    arr = [int(i) for i in input().strip().split(' ')]
    for _ in range(q):
        f, a, b = [int(i) for i in input().strip().split(" ")]
        if f == 1:
            for i in range(a - 1, b):
                arr[i] += 1
        elif f == 2:
            s = 0
            for i in arr[a - 1:b]:
                s += fa(i)
            print(s % 1000000000)
        else:
            arr[a - 1] = b
