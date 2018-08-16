"""
if __name__ == '__main__':
    n = [int(__) for __ in list(input().strip())]
    spotted = None
    for i in range(len(n) - 1, -1, -1):
        num = n[i] + 1
        while num in n[:i] and num != 10:
            num += 1
        if num != 10:
            spotted = i
            n[spotted] = num
            break
    for i in range(spotted + 1, len(n)):
        n[i] = i - spotted - 1
        num = n[i]
        while num in n[:i]:
            num += 1
        n[i] = num
    for i in range(1, len(n)):
        if n[i] in n[:i]:
            dup = i
            num = n[i] + 1
            while num in n[:i]:
                num += 1
            n[i] = num
            for j in range(dup + 1, len(n)):
                n[j] = j - dup - 1
                num = n[j]
                while num in n[:j]:
                    num += 1
                n[j] = num
            break
    print(''.join([str(i) for i in n]))

"""
if __name__ == '__main__':
    n = int(input().strip()) + 1
    while True:
        if len(set(str(n))) == 4:
            print(n)
            break
        n += 1