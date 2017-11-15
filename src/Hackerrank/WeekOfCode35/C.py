"""
3 3
1 3 4
2 2 3
1 2 4

5 4
1 2 3 4 5
3 4 5 6 7
8 9 10 11 1
9 8 8 7 4
"""

if __name__ == '__main__':
    l, b = [int(i) for i in input().strip().split(" ")]
    toy = [[0 for i in range(l + 2)] for j in range(b + 2)]
    for i in range(b):
        inp = [int(j) for j in input().strip().split(" ")]
        for j in range(len(inp)):
            toy[i + 1][j + 1] = inp[j]
    cost = 0
    for i in toy:
        for j in i:
            print(j, end=" ")
        print()
    for i in range(1, l + 1):
        for j in range(1, b + 1):
            if toy[i][j] > toy[i - 1][j]:
                cost += toy[i][j] - toy[i - 1][j]
            if toy[i][j] > toy[i][j - 1]:
                cost += toy[i][j] - toy[i][j - 1]
            if toy[i][j] > toy[i + 1][j]:
                cost += toy[i][j] - toy[i + 1][j]
            if toy[i][j] > toy[i][j + 1]:
                cost += toy[i][j] - toy[i][j + 1]
            cost += 2
    print(cost)
