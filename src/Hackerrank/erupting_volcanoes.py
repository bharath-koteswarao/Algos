def print_matrix(l):
    for i in l:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == '__main__':
    size = int(input())
    num = int(input())
    l = [[0 for j in range(size)] for i in range(size)]
    # print_matrix(l)
    answer = 0
    for test_case in range(num):
        inp = input().split(" ")
        hor, ver, weight = [int(inp[0]), int(inp[1]), int(inp[2])]
        left = hor - (weight - 1)
        right = hor + (weight - 1)
        top = ver - (weight - 1)
        down = ver + (weight - 1)
        for i in range(left, right + 1):
            for j in range(top, down + 1):
                if i < size and j < size:
                    if i is hor and j is ver:
                        l[i][j] += weight
                    elif i - hor is 0:
                        l[i][j] += weight - abs(j - ver)
                    elif j - ver is 0:
                        l[i][j] += weight - abs(i - hor)
                    else:
                        l[i][j] += weight - max(abs(i - hor), abs(j - ver))
                    answer = max(answer, l[i][j])
        print_matrix(l)
    print(answer)
