from sample_tree import get_tree_root


def get_lca(root, n1, n2):
    if root is None:
        return None
    elif root.data == n1 or root.data == n2:
        return root.data
    else:
        left = get_lca(root.left, n1, n2)
        right = get_lca(root.right, n1, n2)
        if left is not None and right is not None:
            return root.data
        elif left is not None:
            return left
        elif right is not None:
            return right
        else:
            return None


if __name__ == '__main__':
    root = get_tree_root()
    a = int(input("Node 1: "))
    b = int(input("Node 2: "))
    lca = get_lca(root, a, b)
    print(lca)
