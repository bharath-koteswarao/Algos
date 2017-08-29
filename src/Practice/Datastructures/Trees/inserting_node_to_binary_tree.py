from collections import deque

from sample_tree import Node
from sample_tree import get_tree_root


def insert_new_node(data, root):
    new_node = Node(data)
    while root.right is not None:
        root = root.right
    # Now root is the right most element of the tree
    root.left = new_node


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
    print()
    data = int(input("Enter new data to be inserted : "))
    insert_new_node(data, root)
    print("After inserting new node : ", end="")
    traverse_by_level_order(root)


main()
