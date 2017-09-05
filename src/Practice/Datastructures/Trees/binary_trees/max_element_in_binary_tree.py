from sample_tree import get_tree_root

maxE = -100


def find_max_element(root):
    global maxE
    left = root.left
    right = root.right
    if left is not None and right is not None:
        find_max_element(left)
        find_max_element(right)
    maxE = max(maxE, root.data)
    return maxE


def main():
    root = get_tree_root()
    print(find_max_element(root))


main()
