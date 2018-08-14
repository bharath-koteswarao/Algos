if __name__ == '__main__':
    for _ in range(int(input().strip())):
        w = input().strip()
        if len(w) > 10:
            print(w[0] + str(len(w) - 2) + w[-1])
        else:
            print(w)
