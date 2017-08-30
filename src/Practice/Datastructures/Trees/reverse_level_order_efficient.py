from collections import deque

from sample_tree import get_tree_root


def get_sequenced_que(root):
    que = deque([])
    sequenced_que = deque([])
    que.append(root)
    que.append(None)
    while len(que) is not 0:
        node = que.popleft()
        sequenced_que.append(node)
        if node is None:
            que.append(None)
            if len(sequenced_que) >= 2:
                if sequenced_que[len(sequenced_que) - 2] is None:
                    break
        else:
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
    return sequenced_que


def main():
    root = get_tree_root()
    sequenced_que = get_sequenced_que(root)
    sequenced_que.pop()
    sequenced_que.pop()
    length = len(sequenced_que)
    stack = []
    for i in range(0, length):
        temp = sequenced_que.pop()
        if temp is None:
            while len(stack) is not 0:
                print(stack.pop(), end=" ")
        else:
            stack.append(temp.data)


main()
