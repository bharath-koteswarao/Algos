import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

if __name__ == '__main__':
    n, x = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    l = []
    for i in range(n):
        l.append((n - i) * arr[i])
    l.sort()
    su = 0
    co = 0
    for i in range(n):
        if su + l[i] <= x:
            su += l[i]
            co += 1
        else:
            break
    print(co)
