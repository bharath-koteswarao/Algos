if __name__ == '__main__':
    n = int(input().strip())
    print("YES" if len(set(list(input().strip().lower()))) == 26 else "NO")
