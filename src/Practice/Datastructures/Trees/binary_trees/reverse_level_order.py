import math
from collections import deque

from sample_tree import get_tree_root


class Pair:
    left = None
    right = None

    def __init__(self, left_data=None, right_data=None):
        self.left = left_data
        self.right = right_data


def get_queue(root):
    que1 = deque([])
    que2 = deque([])
    que1.append(root)
    while len(que1) is not 0:
        node = que1.popleft()
        left_data = None if node.left is None else node.left.data
        right_data = None if node.right is None else node.right.data
        que2.append(Pair(left_data, right_data))
        if node.left is not None:
            que1.append(node.left)
        if node.right is not None:
            que1.append(node.right)
    return que2


def main():
    root = get_tree_root()
    que = get_queue(root)
    stack = [Pair(root.data)]
    for pair in que:
        stack.append(pair)
    size = len(stack) + 1
    number_of_levels = math.log(size, 2)
    number_of_nones = 2 ** (number_of_levels - 1)
    for i in range(0, int(number_of_nones)):
        stack.pop()
    size = len(stack)
    actual_levels = int(math.log(size, 2))
    list_of_levels = [2 ** i for i in range(0, actual_levels)]
    list_of_levels = reversed(list_of_levels)
    print("Reversed level order : ", end="")
    for i in list_of_levels:
        temp = []
        for j in range(0, i):
            temp.append(stack.pop())
        while len(temp) is not 0:
            pair = temp.pop()
            print(pair.left, pair.right, end=" ")


main()
