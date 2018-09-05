def pt(ma):
    print("YES")
    for x in ma:
        print('|'.join(x))


if __name__ == '__main__':
    n = int(input().strip())
    ma = []
    for _ in range(n):
        ma.append(input().strip().split('|'))
    for seat in ma:
        if seat[0] == 'OO':
            seat[0] = '++'
            pt(ma)
            exit(0)
        elif seat[1] == 'OO':
            seat[1] = '++'
            pt(ma)
            exit(0)
    print("NO")
