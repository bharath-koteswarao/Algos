if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    bal = [int(__) for __ in input().strip().split()]
    costs = [int(__) for __ in input().strip().split()]
    l = []
    for i in range(n):
        for j in range(1, bal[i] + 1):
            l.append(costs[i] * j)
    l.sort(reverse=True)
    if k >= len(l):
        print(0)
    else:
        # print(l)
        print(l[k])
