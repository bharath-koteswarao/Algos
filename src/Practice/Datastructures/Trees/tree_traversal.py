from sample_tree import get_tree_root


def print_pre_order(root):
    print(root.data, end=" ")
    left = root.left
    right = root.right
    if left is not None:
        print_pre_order(left)
    if right is not None:
        print_pre_order(right)


def print_post_order(root):
    left = root.left
    right = root.right
    if left is not None:
        print_post_order(left)
    if right is not None:
        print_post_order(right)
    print(root.data, end=" ")


def print_in_order(root):
    left = root.left
    right = root.right
    if left is not None:
        print_in_order(left)
    print(root.data, end=" ")
    if right is not None:
        print_in_order(right)


def main():
    root = get_tree_root()
    print("in-order : ", end="")
    print_in_order(root)
    print()
    print("pre-order : ", end="")
    print_pre_order(root)
    print()
    print("post-order : ", end="")
    print_post_order(root)


main()


# Prints in order,pre order and post order

# in-order : 8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
# pre-order : 1 2 4 8 9 5 10 11 3 6 12 13 7 14 15
# post-order : 8 9 4 10 11 5 2 12 13 6 14 15 7 3 1
