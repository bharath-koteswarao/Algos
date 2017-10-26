from collections import deque

if __name__ == '__main__':
    n, k = [int(i) for i in input().strip().split(" ")]
    inp = [int(i) for i in input().strip().split(" ")]
    if k >= n - 1:
        print(max(inp))
    else:
        q = deque(inp)
        first = q.popleft()
        second = q.popleft()
        winner = 0
        if first > second:
            winner = first
            q.append(second)
        else:
            q.append(first)
            winner = second
        k -= 1
        while k > 0:
            now = q.popleft()
            winner = max(now, winner)
            q.append(min(now, winner))
            k -= 1
        print(winner)
