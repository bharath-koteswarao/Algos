from sample_tree import get_tree_root


def print_pre_order(root):
    print(root.data, end=" ")
    left = root.left
    right = root.right
    if left is not None:
        print_pre_order(left)
    if right is not None:
        print_pre_order(right)


def main():
    root = get_tree_root()
    print_pre_order(root)


main()


# Prints 1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
