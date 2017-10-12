if __name__ == '__main__':
    n = int(input().strip())
    l = []
    for i in range(n):
        l.append(int(input().strip()))
    costs = [1]
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            costs.append(costs[i - 1] + 1)
        else:
            costs.append(1)
    costs2 = [1]
    l = l[::-1]
    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            costs2.append(costs2[-1] + 1)
        else:
            costs2.append(1)
    costs2=costs2[::-1]
    answer = 0
    for i in range(len(costs)):
        answer += max(costs2[i],costs[i])
    print(answer)
