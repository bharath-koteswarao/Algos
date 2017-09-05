from collections import deque

from sample_tree import get_tree_root


def print_level_order(root):
    que = deque([])
    que.append(root)
    while len(que) is not 0:
        node = que.popleft()
        print(node.data, end=" ")
        if node.left is not None:
            que.append(node.left)
        if node.right is not None:
            que.append(node.right)
    print()


def mirror_the_tree(root):
    que = deque([])
    que.append(root)
    while len(que) is not 0:
        node = que.popleft()
        if node.right is not None:
            que.append(node.right)
        if node.left is not None:
            que.append(node.left)
        right = node.right
        left = node.left
        node.right = left
        node.left = right


def main():
    root = get_tree_root()
    print_level_order(root)
    mirror_the_tree(root)
    print_level_order(root)


main()
