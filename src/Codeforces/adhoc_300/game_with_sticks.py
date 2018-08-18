if __name__ == '__main__':
    n, m = [int(__) for __ in input().strip().split()]
    print("Akshat" if min(n, m) % 2 == 1 else "Malvika")
