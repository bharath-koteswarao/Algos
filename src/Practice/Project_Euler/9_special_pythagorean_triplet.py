from math import sqrt


def calculate_product(number):
    found_value = False
    answer = 0
    for n in range(1, number + 1):
        delta = sqrt(n ** 2 + (2 * number))
        if delta - int(delta) == 0:
            m = int((-1 * n + delta) // 2)
            if m != n and m > 0:
                found_value = True
                first = m ** 2 + n ** 2
                second = 2 * m * n
                third = m ** 2 - n ** 2
                answer = max(answer, int(first * second * third))
    if not found_value:
        return -1
    else:
        return int(answer)
    pass


if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        n = int(input().strip())
        ans = calculate_product(n)
        print(ans)
