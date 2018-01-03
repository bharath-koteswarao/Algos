if __name__ == "__main__":
    tc = int(input().strip())
    for _ in range(tc):
        input()
        print("Yes" if sum([int(i) for i in list(''.join(input().strip().split()))]) % 3 == 0 else "No")
