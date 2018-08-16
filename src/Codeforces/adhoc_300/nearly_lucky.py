if __name__ == '__main__':
    n = int(input().strip())
    lu = []
    for i in range(50):
        bi = bin(i)[2:]
        nu = ""
        for x in bi:
            nu += '7' if x == '0' else '4'
        lu.append(int(nu))
    no = 0
    for x in str(n):
        if x == '4' or x == '7':
            no += 1
    print("YES" if no in lu else "NO")
