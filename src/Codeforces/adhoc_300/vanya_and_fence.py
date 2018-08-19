if __name__ == '__main__':
    n, h = [int(__) for __ in input().strip().split()]
    print(sum([1 if int(__) <= h else 2 for __ in input().strip().split()]))