if __name__ == '__main__':
    inp = input().strip()
    le = len(set(inp))
    print("IGNORE HIM!" if le % 2 == 1 else "CHAT WITH HER!")