if __name__ == '__main__':
    sp = int(input().strip())
    if sp <= 90:
        print("0", "No punishment")
    elif 91 <= sp <= 110:
        print(str((sp - 90) * 300), "Warning")
    else:
        print(str((sp - 90) * 500), "License removed")
