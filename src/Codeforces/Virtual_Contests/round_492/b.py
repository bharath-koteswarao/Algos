if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(__) for __ in input().strip().split()]
    ans = []
    for i in range(len(arr)):
        ans.append((arr[i] // n, arr[i] % n, i + 1))
    ans.sort(key=lambda x: (x[0], x[2]))
    # print(ans)
    for i in ans:
        if i[1] < i[2]:
            print(i[2])
            break
