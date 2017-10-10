def collapseThisNumber(i, memo):
    if i in memo:
        return memo[i]
    elif i == 1:
        memo[1] = 0
        return 0
    elif i % 2 == 0:
        temp = collapseThisNumber(i // 2, memo)
        memo[i] = temp + 1
        return temp + 1
    else:
        temp = collapseThisNumber((3 * i) + 1, memo)
        memo[i] = temp + 1
        return temp + 1
    pass


if __name__ == '__main__':
    tc = int(input().strip())
    test_cases = []
    biggest_test_case = 0
    for i_tc in range(tc):
        inp = int(input().strip())
        test_cases.append(inp)
        biggest_test_case = max(biggest_test_case, inp)
    memo = {}
    for i in range(1, biggest_test_case + 1):
        if i not in memo:
            collapseThisNumber(i, memo)
    answers = [0] * (biggest_test_case + 1)
    current_max = 0
    current_answer = 1
    for i in range(1, biggest_test_case + 1):
        if current_max < memo[i]:
            current_max = memo[i]
            current_answer = i
        elif current_max == memo[i]:
            current_answer = i
        answers[i] = current_answer
    for test_case in test_cases:
        print(answers[test_case])
