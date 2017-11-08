if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        inp = list(input().strip())
        a = 0
        b = 0
        non_zero = []
        for i, j in enumerate(inp):
            if j != '.':
                non_zero.append(i)
                if j == 'A':
                    a += 1
                else:
                    b += 1

        for i in range(len(non_zero) - 1):
            if inp[non_zero[i]] == inp[non_zero[i + 1]]:
                if inp[non_zero[i]] == 'A':
                    a += (non_zero[i + 1] - non_zero[i] - 1)
                else:
                    b += (non_zero[i + 1] - non_zero[i] - 1)
        print(a, b)
