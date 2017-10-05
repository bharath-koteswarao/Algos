if __name__ == '__main__':
    tc = int(input())
    for i_tc in range(tc):
        n = int(input())
        sum_of_squares = (n * (n + 1) * ((2 * n) + 1)) // 6
        square_of_sum = ((n * (n + 1)) / 2) ** 2
        print(int(abs(sum_of_squares-square_of_sum)))
