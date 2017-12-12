def fight(h1, a1, c1, h2, a2):
    if h2 <= 0:
        return 0
    else:
        pass
    pass


if __name__ == '__main__':
    h1, a1, c1 = [int(i) for i in input().strip().split(" ")]
    h2, a2 = [int(i) for i in input().strip().split(" ")]
    ans = fight(h1,a1,c1,h2,a2)
