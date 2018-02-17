"""
iuiufgiuiuaahjabbbklboyoyoyoyoyaaaaabbbbbiuiuiuiuiuaaaaabbbbbeyiyuyzyw
"""
if __name__ == '__main__':
    n = int(input().strip())
    w = input().strip()
    n = len(w)
    dic = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
        'y': 0
    }
    i = 0
    ans = w[:]
    while i < n:
        cont = ""
        if w[i] in dic:
            while i < n and w[i] in dic:
                cont += w[i]
                i += 1
            if len(cont) > 1:
                ans = ans.replace(cont,cont[0],1)
        else:
            i += 1
    print(ans)
