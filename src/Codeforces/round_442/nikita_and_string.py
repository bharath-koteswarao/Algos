def contains(temp, inp):
    while len(temp) > 0 and len(inp) > 0:
        if temp[0] == inp[0]:
            temp = temp[1:]
            inp = inp[1:]
        else:
            inp = inp[1:]
    return len(temp) == 0


if __name__ == '__main__':
    a = 0
    b = 0
    inp = input().strip()
    if len(inp) == 1:
        print(1)
    else:
        for i in inp:
            if i == 'a':
                a += 1
            else:
                b += 1
        biggest = 0
        if b == 0:
            print(a)
        elif a == 0:
            print(b)
        else:
            for i in range(1, a + 1):
                for j in range(1, b + 1):
                    temp = ('a' * i) + (j * 'b') + ('a' * (a - i))
                    if contains(temp, inp):
                        biggest = max(len(temp), biggest)
                    temp = ('a' * (a - i)) + (j * 'b') + ('a' * i)
            print(biggest)
