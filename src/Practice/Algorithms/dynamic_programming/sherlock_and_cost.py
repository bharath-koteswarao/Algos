maximum = 0


def sigma(inp):
    ans = 0
    for i in range(0, len(inp) - 1):
        ans += abs(inp[i] - inp[i + 1])
    return ans


def toString(inp):
    ans = ""
    for i in inp:
        ans += str(i)
    return ans


def find(inp, value, memo):
    global maximum
    string = toString(inp)
    if string in memo:
        return memo[string]
    elif value < len(inp):
        least = inp[:]
        highest = inp[:]
        least[value] = 1
        maximum = max(maximum, sigma(least), sigma(highest))
        memo[toString(least)] = sigma(least)
        memo[toString(highest)] = sigma(highest)
        find(least, value + 1, memo)
        find(highest, value + 1, memo)


if __name__ == '__main__':
    tc = int(input())
    input()
    inp = [int(i) for i in input().split(" ")]
    memo = {toString(inp): sigma(inp)}
    find(inp, 0, memo)
    print(memo)
    print(maximum)
