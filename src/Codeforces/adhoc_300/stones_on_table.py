from itertools import groupby

if __name__ == '__main__':
    n = int(input().strip())
    st = input().strip()
    ans = 0
    for x in groupby(st):
        li = list(x[1])
        if len(li) > 1:
            ans += len(li) - 1
    print(ans)
