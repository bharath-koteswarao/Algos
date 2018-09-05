if __name__ == '__main__':
    x, y, z = [int(__) for __ in input().strip().split()]
    print(min(
        2 * (x + z),
        2 * (y + z),
        2 * (x + y),
        x + y + z
    ))
