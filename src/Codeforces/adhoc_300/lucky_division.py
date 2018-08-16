if __name__ == '__main__':
    n = int(input().strip())
    lu = []
    for i in range(8):
        bi = bin(i)[2:]
        nu = ""
        for x in bi:
            nu += '7' if x == '0' else '4'
        lu.append(int(nu))
    for lucky in lu:
        if n % lucky == 0:
            print("YES")
            exit(0)
    print("NO")
