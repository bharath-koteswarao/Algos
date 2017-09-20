from heap_node import HeapNode

"""
This is not 1 based indexing. This is 0 based indexing

Index of last parent is not n/2 if counting starts from 1

Here counting starts from 0.So index of last parent depends on size

If size of heap is even then index of last parent is (size / 2) - 1 else it is (size - 1 / 2)

"""


class MaxHeap:
    length = None
    elements = []

    def __init__(self, input_array):
        self.buildHeap(input_array)
        self.max_heapify(self.elements)
        self.display_heap()

    def buildHeap(self, array):
        self.elements = [HeapNode(i, None, None) for i in array]
        for i in range(len(self.elements)):
            self.elements[i].left = self.elements[2 * i + 1] if (2 * i + 1) < len(self.elements) else None
            self.elements[i].right = self.elements[2 * i + 2] if (2 * i + 2) < len(self.elements) else None

    def getLastParentIndex(self):
        length = len(self.elements)
        if length % 2 is 0:
            return int(length / 2 - 1)
        else:
            return int(((length - 1) / 2) - 1)

    def max_heapify_this_node(self, node):
        # self.display_heap()
        # print()
        if node is None:
            """ Meaning less """
            pass
        elif node.left is None and node.right is None:
            """ Already a heap. No need to change it now"""
            pass
        elif node.left is None:
            if node.data > node.right.data:
                """ Already a heap so no need to change it """
                pass
            else:
                temp = node.data
                node.data = node.right.data
                node.right.data = temp  # Just swapping the two nodes
        elif node.right is None:
            if node.data > node.left.data:
                """ Already a heap so no need to change it """
                pass
            else:
                temp = node.data
                node.data = node.left.data
                node.left.data = temp  # Just swapping the two nodes
        else:
            """ Node has two children and both are valid nodes """
            if node.data is max(node.data, node.right.data, node.left.data):
                """ Already satisfies max heap property"""
                pass
            else:
                """ Find the max node and swap it with root """
                temp = node.data
                if node.right.data > node.left.data:
                    node.data = node.right.data
                    node.right.data = temp
                else:
                    node.data = node.left.data
                    node.left.data = temp

    def max_heapify(self, elements):
        last_parent = self.getLastParentIndex()
        for i in range(last_parent, -1, -1):
            current_node = self.elements[i]
            self.max_heapify_this_node(current_node)
            if current_node.right is not None:
                self.max_heapify_this_node(current_node.right)
            if current_node.left is not None:
                self.max_heapify_this_node(current_node.left)

    def display_heap(self):
        for i in self.elements:
            print(i.data, i.left.data if i.left is not None else None, i.right.data if i.right is not None else None)


if __name__ == "__main__":
    hp = MaxHeap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
