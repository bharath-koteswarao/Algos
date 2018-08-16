if __name__ == '__main__':
    n, t = [int(__) for __ in input().strip().split()]
    arr = list(input().strip())
    while t > 0:
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 'B' and arr[i + 1] == 'G':
                arr[i] = 'G'
                arr[i + 1] = 'B'
                i += 1
            i += 1
        t -= 1
    print(''.join(arr))
