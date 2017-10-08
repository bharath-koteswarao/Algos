if __name__ == '__main__':
    input()
    inp1 = [int(i) for i in input().strip().split(" ")]
    input()
    inp2 = [int(i) for i in input().strip().split(" ")]
    dic = {}
    for i in inp1:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for i in inp2:
        if i in dic:
            dic[i] -= 1
        else:
            dic[i] = 1
    for i in sorted(dic):
        if dic[i] != 0:
            print(i, end=" ")
