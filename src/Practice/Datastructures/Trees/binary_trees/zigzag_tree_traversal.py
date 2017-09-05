from collections import deque

import sample_tree


def print_in_zigzag_order(lis):
    reverse = False
    stack = []
    for i in range(0, len(lis)):
        if not reverse:
            if lis[i] is not None:
                print(lis[i], end=" ")
            else:
                reverse = not reverse
        else:
            if lis[i] is None:
                reverse = not reverse
                while len(stack) is not 0:
                    print(stack.pop(), end=" ")
            else:
                stack.append(lis[i])


def main():
    root = sample_tree.get_tree_root()
    que = deque([])
    que.append(root)
    que.append(None)
    lis = []
    while len(que) is not 0:
        node = que.popleft()
        lis.append(node)
        if node is None:
            que.append(None)
            if len(lis) >= 2:
                first = lis[len(lis) - 1]
                second = lis[len(lis) - 2]
                if first is None and second is None:
                    break

        else:
            if node.left is not None:
                que.append(node.left)
            if node.right is not None:
                que.append(node.right)
    for i in range(0, len(lis)):
        lis[i] = lis[i].data if lis[i] is not None else None
    print_in_zigzag_order(lis)


main()
