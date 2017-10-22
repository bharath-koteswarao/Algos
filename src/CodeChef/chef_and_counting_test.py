if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        inp = input().strip()
        answer = 0
        if len(inp) == 2:
            if inp[0] == inp[1]:
                answer = 1
        else:
            dic = {}
            for i, j in enumerate(inp):
                if j in dic:
                    dic[j].append(i)
                else:
                    dic[j] = [i]
            for letter in dic:
                occ = dic[letter]
                if len(occ) == 2:
                    if occ[1] - occ[0] == 1:
                        answer += 1
                    else:
                        answer += 1 if len(set(inp[occ[0] + 1:occ[1]])) == 1 else 0
                elif len(occ) > 2:
                    for i in range(len(occ)):
                        for j in range(i + 1, len(occ)):
                            if occ[j] - occ[i] == 1:
                                answer += 1
                            else:
                                answer += 1 if len(set(inp[occ[i + 1] + 1:occ[j]])) == 1 else 0
        print(answer)
