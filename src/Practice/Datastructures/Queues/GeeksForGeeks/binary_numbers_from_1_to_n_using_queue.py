from collections import deque

tc = int(input())
for j in range(0, tc):
    n = int(input())
    que = deque(["1"])
    for i in range(0, n):
        temp = que.popleft()
        print(temp, end=" ")
        que.append(temp + "0")
        que.append(temp + "1")
    print()
