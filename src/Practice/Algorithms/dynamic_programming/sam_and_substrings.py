def convert(str_num):
    num = 0
    mul = 1
    for i in range(len(str_num)-1,-1,-1):
        num += str_num[i] * mul
        mul *= 10
    return num


if __name__ == '__main__':
    inp = int(input())
    l = []
    while inp > 0:
        l.append(inp%10)
        inp //= 10
    l = l[::-1]
    count = 0
    answer = 0
    for i in range(0,len(l)):
        for j in range(0,len(l) - count):
            str_num = (l[j:j+count+1])
            int_num = convert(str_num)
            answer += int_num
        count += 1
    print(answer)
