if __name__ == '__main__':
    tc = int(input().strip())
    pos = [0, 0, 1, 1, 1, 1, 1]
    for _ in range(tc):
        print("Second" if not pos[int(input().strip()) % 7] else "First")
