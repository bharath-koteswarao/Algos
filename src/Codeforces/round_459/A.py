if __name__ == '__main__':
    fib = [1, 1]
    while fib[-1] < 1000:
        fib.append(fib[-1] + fib[-2])
    n = int(input().strip())
    arr = ['o'] * n
    for i in fib:
        if i <= n:
            arr[i - 1] = 'O'
        else:
            break
    print(''.join(arr))