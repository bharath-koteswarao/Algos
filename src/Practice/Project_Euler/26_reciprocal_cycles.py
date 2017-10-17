from pprint import pprint as pp


def number_recurs(num):
    if num % 3 == 0 or num % 7 == 0:
        return True
    return False


if __name__ == '__main__':
    dic = {}
    current_highest = -1
    current_highest_num = 0
    tc = int(input().strip())
    test_cases = []
    for i_tc in range(tc):
        test_cases.append(int(input().strip()))
    biggest_tc = max(test_cases)
    for i in range(1, biggest_tc + 1):
        if number_recurs(i):
            recur_len = len(set(str(1 / i)[2:]))
            if recur_len > current_highest:
                current_highest = recur_len
                current_highest_num = i
        dic[i] = current_highest_num
    pp(dic, width=1)
    for test_case in test_cases:
        print(dic[test_case - 1])
