def digSum(n):
    ret = 0
    while n > 0:
        ret += n % 10
        n = n // 10
    return ret


def calc(n, d):
    count = 1000
    ans, steps = 11, float('inf')
    visited = {}
    current = [n]
    level = 0
    while count > 0:
        count -= 1
        next = []
        for x in current:
            if x < ans:
                ans = x
                steps = level
            elif x == ans and level < steps:
                steps = level
            if x + d not in visited:
                visited[x + d] = 1
                next.append(x + d)
            digS = digSum(x)
            if digS not in visited:
                visited[digS] = 1
                next.append(digS)
        level += 1
        current = next[:]
    return str(ans) + " " + str(steps)


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, d = [int(__) for __ in input().strip().split()]
        print(calc(n, d))
