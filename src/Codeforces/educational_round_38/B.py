if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    first = []
    second = [0 for i in range(len(arr))]
    for i in arr:
        first.append(i-1)
    for j in range(len(arr) - 1,-1,-1):
        second[j] = abs(10 ** 6 - arr[j])
    print(first)
    print(second)
    found = False
    for i in range(len(arr)):
        if first[i] >= second[i]:
            found = True
            ans = first[i-1]