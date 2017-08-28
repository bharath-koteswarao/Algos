class Node:
    left = None  # Left Node
    right = None  # Right Node
    data = 0  # Node data

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def main():
    # Generate a simple tree for further calculations

    one = int(input("First data : "))
    two = int(input("Second data : "))
    three = int(input("Third data : "))
    four = int(input("Fourth data : "))
    five = int(input("Fifth data : "))
    six = int(input("Sixth data : "))
    seven = int(input("Seventh data : "))
    eight = int(input("Eighth data : "))
    nine = int(input("Ninth data : "))
    ten = int(input("Tenth data : "))
    eleven = int(input("Eleventh data : "))
    twelve = int(input("Twelfth data : "))
    thirteen = int(input("Thirteenth data : "))
    fourteen = int(input("Fourteenth data : "))
    fifteen = int(input("Fifteenth data : "))

    eighth = Node(eight)
    ninth = Node(nine)
    tenth = Node(ten)
    eleventh = Node(eleven)
    twelfth = Node(twelve)
    thirteenth = Node(thirteen)
    fourteenth = Node(fourteen)
    fifteenth = Node(fifteen)
    fourth = Node(four, eighth, ninth)
    fifth = Node(five, tenth, eleventh)
    sixth = Node(six, twelfth, thirteenth)
    seventh = Node(seven, fourteenth, fifteenth)
    second = Node(two, fourth, fifth)
    third = Node(three, sixth, seventh)
    root = Node(one, second, third)
    return root


def get_tree_root():
    return main()
