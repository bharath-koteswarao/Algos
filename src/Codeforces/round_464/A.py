if __name__ == '__main__':
    n = int(input().strip())
    found = False
    arr = [int(i) for i in input().strip().split()]
    dic = {}
    for i in range(len(arr)):
        dic[i + 1] = arr[i]
    for i in dic:
        x = dic[i]
        if x in dic:
            y = dic[x]
            if y in dic:
                if dic[y] != i:
                    pass
                else:
                    found = True
                    break
    print("YES" if found else "NO")
