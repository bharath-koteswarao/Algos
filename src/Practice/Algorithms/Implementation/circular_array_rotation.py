from collections import deque

if __name__ == '__main__':
    n, k, qu = [int(i) for i in input().strip().split(" ")]
    q = deque([int(i) for i in input().strip().split(" ")])
    q.rotate(k)
    for i in range(qu):
        print(q[int(input().strip())])
