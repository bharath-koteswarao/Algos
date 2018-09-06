if __name__ == '__main__':
    n = int(input().strip())
    a1 = [int(__) for __ in input().strip().split()]
    a2 = [int(__) for __ in input().strip().split()]
    a1.sort(reverse=True)
    a2.sort(reverse=True)
    i, j = 0, 0
    ct = 0
    s1, s2 = 0, 0
    while True:
        if i == n and j == n:
            break
        else:
            if ct % 2 == 0:
                # p1
                if i == n:
                    j += 1
                elif j == n:
                    s1 += a1[i]
                    i += 1
                else:
                    if a1[i] > a2[j]:
                        s1 += a1[i]
                        i += 1
                    elif a1[i] == a2[j]:
                        s1 += a1[i]
                        i += 1
                    else:
                        j += 1
            else:
                # p2
                if j == n:
                    i += 1
                elif i == n:
                    s2 += a2[j]
                    j += 1
                else:
                    if a2[j] > a1[i]:
                        s2 += a2[j]
                        j += 1
                    elif a2[j] == a1[i]:
                        s2 += a2[j]
                        j += 1
                    else:
                        i += 1
        ct += 1
    print(s1 - s2)
