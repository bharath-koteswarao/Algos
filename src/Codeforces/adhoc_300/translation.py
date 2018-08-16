if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    print("YES" if b == a[::-1] else "NO")