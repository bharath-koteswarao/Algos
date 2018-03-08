from collections import Counter as c

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        cou = c(arr)
        valid = True
        for i in cou:
            if cou[i] != 1:
                valid = False
                break
        if valid:
            print(0)
        else:
            ans = 0
            for i in cou:
                if cou[i] > 1:
                    ans += cou[i] - 1
            print(ans)
