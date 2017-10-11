def compare(year, month, final_year, final_month):
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
    if final_month == 1:
        final_month = 13
        final_year -= 1
    elif final_month == 2:
        final_year -= 1
        final_month = 14
    return year == final_year and month == final_month
    pass


def calculate(year, month, day=1):
    if month == 1:
        month = 13
        year -= 1
    elif month == 2:
        month = 14
        year -= 1
    k = year % 100
    j = year // 100
    m = month
    q = 1
    return int((q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) + (5 * j))) % 7
    pass


if __name__ == '__main__':
    tc = int(input().strip())
    for i_tc in range(tc):
        first = [int(i) for i in input().strip().split(" ")]
        second = [int(i) for i in input().strip().split(" ")]
        year, month, day = first
        count = 0
        if day != 1:
            day = 1
            month += 1
            if not (month == 2 and day > 28 and year % 4 == 0):
                if calculate(year, month, day) == 1:
                    count += 1
        while True:
            calculated_day = calculate(year, month, 1)
            if calculated_day == 1:
                count += 1
            month += 1
            if month > 12:
                year += 1
                month = 1
            if compare(year, month, second[0], second[1]):
                break
        if calculate(second[0], second[1]) == 1:
            count += 1
        print(count)
