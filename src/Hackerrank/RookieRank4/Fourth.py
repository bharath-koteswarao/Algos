from itertools import combinations as comb

if __name__ == '__main__':
    n, m, x = [int(__) for __ in input().strip().split()]
    arr = [int(__) for __ in input().strip().split()]
    l = []
    ans = 0
    for i in range(1, n + 1):
        l.append(list(comb(arr, i)))
    for i in l:
        for j in i:
            pro = 1
            for k in j:
                pro *= k
            if pro % m == x:
                ans += 1
    print(ans)
