from pprint import pprint as pp

if __name__ == '__main__':
    n = int(input().strip())
    d1, d2 = {}, {}
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            if i ** j in d1:
                d1[i ** j].append((i, j))
            else:
                d1[i ** j] = [(i, j)]
    pp(d1, width=1)
    print(len(d1) + len(d2))
