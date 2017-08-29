from collections import deque

from sample_tree import get_tree_root


def traverse_by_level_order(root):
    q = deque([])
    q.append(root)
    print("Level order traversal : ", end="")
    while len(q) is not 0:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)


def main():
    root = get_tree_root()
    traverse_by_level_order(root)


main()

#   Level order traversal : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
