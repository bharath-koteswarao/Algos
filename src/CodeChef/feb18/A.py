if __name__ == '__main__':
    for _ in range(int(input().strip())):
        inp = input().strip()
        ans = 0
        for i in range(len(inp) - 3):
            dic = {'c': 0, 'h': 0, 'e': 0, 'f': 0}
            for j in range(i, i + 4):
                if inp[j] in dic:
                    del dic[inp[j]]
            if len(dic) == 0:
                ans += 1
        print("normal" if ans == 0 else "lovely " + str(ans))
