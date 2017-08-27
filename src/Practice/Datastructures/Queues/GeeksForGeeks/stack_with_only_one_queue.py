from collections import deque


def main():
    items = [1, 2, 3, 4, 5]
    queue = deque(items)
    push(queue, 10)
    pop(queue)


main()


def pop(queue):
    queue.popleft();


def push(queue, item):
    queue.append(item)
    size = len(queue)
    for i in range(size):
        queue.append(queue.popleft())
