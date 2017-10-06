from collections import deque

if __name__ == '__main__':
    n, c = [int(i) for i in input().strip().split(" ")]
    q = deque([int(i) for i in input().strip().split(" ")])
    index_total = []
    count = 0
    store = 0
    for i in range(c):
        tc = [int(j) for j in input().strip().split()]
        if tc[0] == 1:
            x = tc[1]
            store += x
        elif tc[0] == 2:
            y = tc[1]
            store -= y
        elif tc[0] == 3:
            q.rotate(store)
            index_total = []
            for p in range(len(q)):
                count += q[p]
                index_total.append(count)
            store = 0
            l = tc[1]
            r = tc[2]
            if l-1 >= 0:
                print(index_total[r] - index_total[l-1])
            else:
                print(index_total[r])
