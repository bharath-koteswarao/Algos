if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split(" ")]
    dic = {}
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30,
         31, 30, 31, 31, 30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x = str(m)[1:-1]
    y = str(arr)[1:-1]
    r = y.replace('29', '28')
    if (y in x or r in x) and arr.count(29) < 2:
        print("YES")
    else:
        print("NO")
