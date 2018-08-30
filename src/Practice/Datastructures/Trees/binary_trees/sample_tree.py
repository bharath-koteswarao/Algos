class Node:
    left = None  # Left Node
    right = None  # Right Node
    data = 0  # Node getData

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


def main():
    # Generate a simple tree for further calculations
    l = input("Enter fifteen numbers : ").strip().split()
    l = [int(i) for i in l]

    eighth = Node(l[7])
    ninth = Node(l[8])
    tenth = Node(l[9])
    eleventh = Node(l[10])
    twelfth = Node(l[11])
    thirteenth = Node(l[12])
    fourteenth = Node(l[13])
    fifteenth = Node(l[14])
    fourth = Node(l[3], eighth, ninth)
    fifth = Node(l[4], tenth, eleventh)
    sixth = Node(l[5], twelfth, thirteenth)
    seventh = Node(l[6], fourteenth, fifteenth)
    second = Node(l[1], fourth, fifth)
    third = Node(l[2], sixth, seventh)
    root = Node(l[0], second, third)
    return root


def get_tree_root():
    return main()
