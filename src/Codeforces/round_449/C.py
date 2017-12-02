def f(k, dic):
    for i in range(1, k + 1):
        dic[i] = "What are you doing while sending \"" + dic[i - 1] + "\"? Are you busy? Will you send \"" + dic[
            i - 1] + "\"?"


if __name__ == '__main__':
    q = int(input().strip())
    lis = []
    m = 0
    for _ in range(q):
        n, k = [int(i) for i in input().strip().split(" ")]
        m = max(m, n)
        lis.append((n, k))
    dic = {0: "What are you doing at the end of the world? Are you busy? Will you save us?"}
    f(m, dic)
    for i in lis:
        a, b = i
        s = dic[a]
        if b > len(s):
            print('.', end="")
        else:
            print(s[b - 1], end="")
