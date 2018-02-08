if __name__ == '__main__':
    n, k = [int(i) for i in input().strip().split()]
    if n == k:
        if n == 1:
            print("Yes")
        else:
            print("No")
    elif k >= n:
        print("No")
    else:
        if n % 2 == 0:
            if n == 2:
                print("Yes")
            else:
                print("No")
        else:
            pass
