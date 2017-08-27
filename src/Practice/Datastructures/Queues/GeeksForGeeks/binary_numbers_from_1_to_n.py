tc = int(input())

for j in range(0, tc):
    n = int(input())

    pattern = "{0:b}"

    for i in range(1, n + 1):
        print(pattern.format(i), end=" ")
    print()
