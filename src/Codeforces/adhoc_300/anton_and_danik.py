if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    a, d = s.count('A'), s.count('D')
    if a == d:
        print("Friendship")
    elif a > d:
        print("Anton")
    else:
        print("Danik")
