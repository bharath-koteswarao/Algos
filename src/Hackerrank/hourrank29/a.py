if __name__ == '__main__':
    for __ in range(int(input().strip())):
        n = int(input().strip())
        arr = []
        for _ in range(n):
            arr.append(input().strip().split())
        start = arr[0][0]
        crct = []
        for i in range(n):
            if i == 0:
                start = arr[0][0]
            else:
                start = '1' if arr[i - 1][0] == '0' else '0'
            l = [start]
            for j in range(1, n):
                l.append('0' if l[j - 1] == '1' else '1')
            crct.append(l)
        # print(crct)
        print("Yes" if crct == arr else "No")
