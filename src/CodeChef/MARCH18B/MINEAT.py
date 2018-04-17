"""
1
1 3
4
"""
def possible(idx, dif, num=None):
    if not num:
        rem = pre[-1] - pre[idx] - (n - 1 - idx) * arr[idx]
        poss = arr[idx] * dif >= rem
        return poss
    else:
        rem = pre[-1] - pre[idx] - (n - 1 - idx) * num
        poss = num * dif >= rem
        return poss


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, h = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        arr.sort()
        # print(arr)
        pre = [arr[0]]
        for __ in range(1, n):
            pre.append(pre[__ - 1] + arr[__])
        total = sum(arr)
        sma = min(arr)
        big = max(arr)
        if h == n:
            print(big)
        else:
            dif = h - n
            left, right, idx = 0, 0, 0
            hit = False
            for i in range(n - 2, -1, -1):
                if not possible(i, dif):
                    left = arr[i]
                    right = arr[i + 1]
                    hit = True
                    idx = i
                    break
            ans = 0
            left = 1
            right = arr[0] if not hit else right
            while right != left:
                mid = (right + left) // 2
                if possible(idx=idx, dif=dif, num=mid):
                    right = mid
                else:
                    left = mid + 1
            print(right)
            # print(left,right)
            # for i in range(right, left - 1, -1):
            #     if possible(idx=idx, dif=dif, num=i):
            #         ans = i
            #     else:
            #         break
            # print(ans)
