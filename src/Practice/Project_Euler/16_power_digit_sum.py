if __name__ == '__main__':
    tc = int(input().strip())
    for i in range(tc):
        print(sum([int(j) for j in list(str(int(2 ** int(input().strip()))))]))