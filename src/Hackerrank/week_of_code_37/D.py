from collections import defaultdict


def correct(tup, q):
    return int((q - tup[1]) / tup[0]) == (q - tup[1]) / tup[0]


if __name__ == '__main__':
    dic = defaultdict(int)
    for _ in range(int(input().strip())):
        ip = input().strip().split()
        if ip[0] == '+':
            ip[1] = int(ip[1])
            ip[2] = int(ip[2])
            dic[(ip[1], ip[2])] += 1
        elif ip[0] == '-':
            ip[1] = int(ip[1])
            ip[2] = int(ip[2])
            dic[(ip[1], ip[2])] -= 1
        else:
            q = ip[1]
            q = int(q)
            ans = 0
            for i in dic:
                if correct(i, q):
                    ans += dic[i]
            print(ans)
