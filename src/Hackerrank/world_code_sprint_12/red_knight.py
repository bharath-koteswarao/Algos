if __name__ == '__main__':
    _ = int(input().strip())
    __, ___, ____, _____ = [int(______) for ______ in input().strip().split(" ")]
    if abs(_____ - ___) % 2 == 1 or abs(____ - __) % 2 == 1:
        print("Impossible")
    elif __ == ___:
        if ____ < _____:
            while ____ != _____:
                ____ += 2
                print("R", end=" ")
        else:
            while ____ != _____:
                ____ -= 2
                print("L", end=" ")
    elif ____ == _____:
        if __ < ____:
            while __ != ____:
                print("UL", end=" ")
                __ += 1
        else:
            while __ != ____:
                print("LL", end=" ")
                __ -= 1
