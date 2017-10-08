if __name__ == '__main__':
    inp = [int(i) for i in input("Give Input Array : ").strip().split(" ")]
    """
    Each element occurs even times except one element that occurs odd times
    """
    xor = 0
    for i in inp:
        xor ^= i
    print(xor)