if __name__ == '__main__':
    inp = input().strip()
    zero = 0
    one = 0
    first_index = -1
    fs = False
    for i in range(len(inp)):
        if inp[i] == '1':
            one += 1
            if not fs:
                first_index = i
                fs = True
    if first_index == -1:
        print("NO")
    else:
        for i in range(first_index, len(inp)):
            if inp[i] == '0':
                zero += 1
        if zero >= 6:
            print("YES")
        else:
            print("NO")
