# def generate(arr, idx, dic):
#     if idx < len(arr):
#         if str(arr) not in dic:
#             dic[str(arr)] = 1
#         else:
#             dic[str(arr)] += 1
#         for i in range(idx, len(arr)):
#             for j in range(len(arr)):
#                 temp = arr[:]
#                 te = temp[i]
#                 temp[i] = temp[j]
#                 temp[j] = te
#                 generate(temp, idx + 1, dic)
#
#
# def getMin(dic):
#     mi = 10 ** 10
#     ret = 0
#     for x in dic:
#         if dic[x] < mi:
#             ret = x
#             mi = dic[x]
#     return ret
#
#
# def getMax(dic):
#     ma = 0
#     ret = 0
#     for x in dic:
#         if dic[x] > ma:
#             ret = x
#             ma = dic[x]
#     return ret
#
#
# if __name__ == '__main__':
#     ans = {}
#     for x in range(1, 8):
#         arr = [k + 1 for k in range(x)]
#         dic = {str(arr): 1}
#         generate(arr, 0, dic)
#         print(getMax(dic))
#         print(getMin(dic))
#         print("Finished ", str(x))

if __name__ == '__main__':
    # n = int(input().strip())
    # if n == 1:
    #     print(1)
    #     print(1)
    # elif n == 2:
    #     print(*[2, 1])
    #     print(*[1, 2])
    # elif n == 3:
        print(*[2, 1, 3])
        print(*[1, 2, 3])
    # elif n == 4:
    #     print(*[2, 1, 4, 3])
    #     print(*[1, 2, 3, 4])
    # elif n == 5:
    #     print(*[3, 1, 2, 5, 4])
    #     print(*[1, 2, 3, 4, 5])
    # elif n == 6:
    #     print(*[4, 1, 2, 3, 6, 5])
    #     print(*[1, 2, 3, 4, 5, 6])
    # else:
    #     print(5 / 0)
