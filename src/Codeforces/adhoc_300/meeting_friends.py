if __name__ == '__main__':
    arr = [int(__) for __ in input().strip().split()]
    print(max(arr) - min(arr))