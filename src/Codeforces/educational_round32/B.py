if __name__ == '__main__':
    input()
    inp = list(input().strip())
    dic = {"L": 0,
           "D": 0,
           "U": 0,
           "R": 0}
    for i in inp:
        dic[i] += 1
    count = 0
    count += min(dic['L'], dic['R']) * 2
    count += min(dic['U'], dic['D']) * 2
    print(count)
