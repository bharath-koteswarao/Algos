from sample_tree import get_tree_root

found = False


def is_there_any_path(root, SUM):
    if root is not None:
        global found
        SUM -= root.data
        if SUM <= 0:
            if SUM is 0:
                found = True
        else:
            is_there_any_path(root.left, SUM)
            is_there_any_path(root.right, SUM)


def main():
    root = get_tree_root()
    SUM = int(input("Enter a number to check existence of a path : "))
    is_there_any_path(root, SUM)
    print("Path exists" if found else "No path exists to get this sum from root")


main()
