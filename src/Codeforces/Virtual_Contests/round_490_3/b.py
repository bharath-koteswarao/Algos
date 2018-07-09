if __name__ == '__main__':
    l = int(input().strip())
    st = input().strip()
    for i in range(2, l + 1):
        if l % i == 0:
            st = st[:i][::-1] + st[i:]
    print(st)
