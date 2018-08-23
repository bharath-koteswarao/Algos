if __name__ == '__main__':
    dic = {}
    for _ in range(int(input().strip())):
        s = input().strip()
        if s not in dic:
            print("OK")
            dic[s] = 1
        else:
            print(s + str(dic[s]))
            dic[s] += 1
