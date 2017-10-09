if __name__ == '__main__':
    tc = int(input().strip())
    total = 0
    for i_tc in range(tc):
        total += int(input().strip())
    print(str(total)[:10])