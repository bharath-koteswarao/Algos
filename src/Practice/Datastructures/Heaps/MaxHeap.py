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

    def buildHeap(self, array):
        self.elements = [HeapNode(i, None, None) for i in array]
        for i in range(len(self.elements)):
            self.elements[i].left = self.elements[2 * i + 1] if (2 * i + 1) < len(self.elements) else None
            self.elements[i].right = self.elements[2 * i + 2] if (2 * i + 2) < len(self.elements) else None

    def getMaxNode(self):
        return self.elements[0]

    def getParent(self, position):
        parent_index = int((position - 2) / 2) if position % 2 is 0 else int((position - 1) / 2)
        return self.getNode(parent_index)

    def extract_max_node(self):
        # Max node is the first node in the heap
        # The process of extracting the max node of heap is as follows:
        # Get the first element and store it to return
        # Now replace the first element with last element and remove the last element
        first_node = self.elements[0]
        last_node = self.elements[len(self.elements) - 1]
        temp = first_node.data
        first_node.data = last_node.data
        last_node.data = temp
        parent = self.getParent(len(self.elements) - 1)
        if parent.right is None:
            parent.left = None
        else:
            parent.right = None
        # After truncating the heap we have to remove the pointer of parent to this node
        self.elements = self.elements[:len(self.elements) - 1]
        self.balance_heap_after_extracting()
        return last_node

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

    def getLastParent(self):
        return self.elements[self.getLastParentIndex()]

    def getNode(self, position):
        return self.elements[position]

    def max_heapify(self, elements):
        last_parent = self.getLastParentIndex()
        for i in range(last_parent, -1, -1):
            current_node = self.getNode(i)
            self.max_heapify_this_node(current_node)
            for j in range(i + 1, last_parent + 1, 1):
                # Here the loop runs from i + 1 since the current node is already
                # Heapified and no point in doing it again
                # So it heapifies every node after this node from top to bottom fashion
                self.max_heapify_this_node(self.getNode(j))

    def display_heap(self):
        for i in self.elements:
            print(i.data, i.left.data if i.left is not None else None, i.right.data if i.right is not None else None)

    def balance_heap_after_extracting(self):
        # This method runs after extracting the max element of heap
        last_parent_index = self.getLastParentIndex()
        for i in range(0, last_parent_index + 1):
            self.max_heapify_this_node(self.getNode(i))

    def heap_sort(self):
        # Running this method will empty the heap
        while len(self.elements) is not 0:
            print(self.extract_max_node().data, end=", ")


if __name__ == "__main__":
    hp = MaxHeap([i for i in range(1, 16)])
    hp.display_heap()
    print("Heap sort : ", end=" ")
    hp.heap_sort()
