if __name__ == '__main__':
    n = int(input().strip())
    s = input().strip()
    if len(s) == 1:
        print("Yes")
    else:
        if len(set(s)) == n:
            print("No")
        else:
            print("Yes")
