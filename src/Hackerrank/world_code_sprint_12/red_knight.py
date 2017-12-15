if __name__ == '__main__':
    n = [int(i) for i in input().strip().split(" ")]
    x1, y1, x2, y2 = [int(i) for i in input().strip().split(" ")]
    if abs(x1 - x2) % 2 == 1:
        print("Impossible")
    elif x1 == x2:
        print(abs(y1 - y2) // 2)
        while y1 != y2:
            if y1 < y2:
                print("R", end=" ")
                y1 += 2
            else:
                print("L", end=" ")
                y1 -= 2
    elif y1 == y2:
        count = 0
        print(abs(x1 - x2) // 2)
        while x1 != x2:
            if x1 < x2:
                x1 += 2
                print("LR" if count % 2 == 0 else "LL", end=" ")
            else:
                x1 -= 2
                print("UL" if count % 2 == 0 else "UR", end=" ")
            count += 1
    else:
        if x2 < x1 and y2 > y1:

            # top right
            pass
        elif x2 > x1 and y2 > y1:
            # bottom right
            pass
        elif x2 > x1 and y2 < y1:
            # bottom left
            pass
        elif x2 < x1 and y2 < y1:
            # top left
            pass
