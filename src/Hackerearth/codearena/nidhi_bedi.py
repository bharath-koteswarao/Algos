def get_max(n, dic):
    if n <= 11:
        return n
    else:
        if n in dic:
            return dic[n]
        else:
            dic[n] = max(get_max(n // 2, dic) + get_max(n // 3, dic) + get_max(n // 4, dic), n)
        return dic[n]


if __name__ == '__main__':
    dic = {}
    while True:
        n = input()
        if n:
            ans = get_max(int(n), dic)
            print(ans)
        else:
            break
            # for i in lis:
            #     n = int(i.strip())
            #     ans = get_max(n)
            #     print(ans)
