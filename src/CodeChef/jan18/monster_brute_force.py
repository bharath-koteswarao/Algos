if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    alive = n
    for _ in range(int(input().strip())):
        x, y = [int(i) for i in input().strip().split()]
        for i in range(1,len(arr) + 1):
            if x & i == i:
                arr[i - 1] -= y
                if arr[i - 1] < 0:
                    alive -= 1
        print(alive)
