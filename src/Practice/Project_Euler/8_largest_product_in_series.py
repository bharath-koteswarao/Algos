# todo
"""
This solution has to be optimised
"""

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(i) for i in input().strip().split()]
        num = [int(i) for i in list(input().strip())]
        ma = 0
        for i in range(n - k):
            temp = 1
            for j in range(i, i + k):
                temp *= num[j]
                if temp == 0:
                    break
            ma = max(ma, temp)
        print(ma)
