from csv import *

file = open("temp.csv", "r")
re = reader(file)

print("Enter two space separated integers like 2 3")
row, col = [int(i) for i in input().strip().split()]

row -= 1
col -= 1

ans = ""
i = 0
for line in re:
    if i == row:
        li = list(line)
        ans = li[col]
    i += 1

print(ans)
file.close()
