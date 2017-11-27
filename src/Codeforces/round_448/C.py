from bisect import bisect_left as bs

if __name__ == '__main__':
    input()
    inp = [int(i) for i in input().strip().split(" ")]
    inp = sorted(inp)
    m = inp[-1]
    squares = []
    dic = {}
    for i in range(len(inp)):
        dic[inp[i]] = i
    for i in range(1, m + 1):
        squares.append(i ** 2)
    print(inp)
    ans = 0
    for i in squares:
        if i ** 0.5 in dic:
            ans += 1
            r = int(i ** 0.5)
            if 1 <= dic[r] <= len(inp) - 2:
                if inp[dic[r - 1]] * inp[dic[r + 1]] == i:
                    ans += 1
        else:
            ind = bs(inp, i ** 0.5, 0, len(inp))
            if inp[ind] * inp[ind - 1] == i:
                ans += 1
    print(ans)
