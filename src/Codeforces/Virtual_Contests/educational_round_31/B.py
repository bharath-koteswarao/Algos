if __name__ == '__main__':
    n, l = [int(i) for i in input().strip().split(" ")]
    arr = [int(i) for i in input().strip().split(" ")]
    s = 0
    for i in arr:
        s += i
    if s + len(arr) - 1 == l:
        print("YES")
    else:
        print("NO")
