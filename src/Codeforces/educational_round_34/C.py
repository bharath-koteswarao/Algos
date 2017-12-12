if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    s = set(arr)
    if len(arr) == len(s):
        print(1)
    elif len(s) == 1:
        print(len(arr))
    else:
        ans = 0
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            ans = max(ans, dic[i])
        print(ans)
