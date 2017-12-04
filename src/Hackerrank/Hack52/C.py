"""
7 5
6 5 1 2 4 6 1
1 7
2 7
1 6
3 6
2 5
"""
if __name__ == '__main__':
    n, q = [int(i) for i in input().strip().split(" ")]
    arr = [int(i) for i in input().strip().split(" ")]
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]].append(i + 1)
        else:
            dic[arr[i]] = [i + 1]
    for _ in range(q):
        l,r = [int(i) for i in input().strip().split(" ")]
        lis = arr
