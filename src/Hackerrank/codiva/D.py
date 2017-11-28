if __name__ == '__main__':
    n, q = [int(i) for i in input().strip().split(" ")]
    arr = [0 for i in range(n)]
    for _ in range(q):
        inp = [int(i) for i in input().strip().split(" ")]
        l = inp[1] - 1
        r = inp[2] - 1
        if inp[0] == 1:
            val = inp[3]
            for i in range(l, r + 1):
                arr[i] ^= val
        elif inp[0] == 2:
            ind = []
            for i in range(l, r + 1):
                if arr[i] == 1:
                    ind.append(i)
            mi = r - l + 1
            for i in range(len(ind) - 1):
                mi = min(mi, ind[i + 1] - ind[i])
            print(mi)
        else:
            i, j = l, r
            while i < r:
                if arr[i] == 1:
                    break
                i += 1
            while j >= i:
                if arr[j] == 1:
                    break
                j -= 1
            if j - i > 0:
                print(j - i)
            else:
                print(-1)
