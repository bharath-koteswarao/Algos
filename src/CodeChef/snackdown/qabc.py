if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        a1 = [int(__) for __ in input().strip().split()]
        a2 = [int(__) for __ in input().strip().split()]
        no = "NIE"
        yes = "TAK"
        s1, s2 = sum(a1), sum(a2)
        if abs(s1 - s2) % 6 != 0:
            print(no)
        else:
            times = abs(s1 - s2) / 6
            cur = [a1]
            while times > 0:
                times -= 1
                next = []
                for x in cur:
                    for i in range(len(x) - 2):
                        new = x[:]
                        new[i] += 1
                        new[i + 1] += 2
                        new[i + 2] += 3
                        next.append(new)
                cur = next[:]
            print("TAK" if a2 in cur else "NIE")
