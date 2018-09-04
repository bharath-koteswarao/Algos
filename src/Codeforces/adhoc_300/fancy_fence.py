if __name__ == '__main__':
    for _ in range(int(input().strip())):
        angle = int(input().strip())
        print("YES" if int(360 / (180 - angle)) == 360 / (180 - angle) else "NO")
