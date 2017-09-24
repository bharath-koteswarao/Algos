def min_edits(s1, s2, memo):
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    elif len(s1) == 0 and len(s2) == 0:
        memo[(s1, s2)] = 0
        return 0
    elif len(s1) == 0 or len(s2) == 0:
        memo[(s1, s2)] = float("inf")
        return float("inf")
    elif s1[0] == s2[0]:
        memo[(s1, s2)] = min_edits(s1[1:], s2[1:], memo)
        return memo[(s1, s2)]
    else:
        replace = min_edits(s2[0] + s1[1:], s2,
                            memo) + 1  # Replace the first character of first string with that of second one
        insert = min_edits(s2[0] + s1, s2, memo) + 1  # Adds the first character of second string to first one
        delete = min_edits(s1[1:], s2, memo) + 1  # delete first character of first string
        return min(
            insert,
            replace,
            delete
        )


if __name__ == '__main__':
    tc = int(input())
    for i_tc in range(tc):
        input()
        (s1, s2) = input().split(" ")
        memo = {}
        answer = min_edits(s1, s2, memo)
        print(answer)
