if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(" ")))
        if n == 1:
            print(0)
            print(arr[0])
        elif n == 2:
            if arr[0] == arr[1]:
                print(0)
                print(arr[0], arr[1])
            else:
                print(2)
                print(arr[1], arr[2])
        elif n == 3:
            s = len(set(arr))
            if s == 1:
                print(0)
                print(arr[0], arr[1], arr[2])
            elif s == 2:
                print(2)
                print(arr[2], arr[0], arr[1])
            else:
                print(3)
                print(arr[2], arr[1], arr[0])
        else:
            temp = []
