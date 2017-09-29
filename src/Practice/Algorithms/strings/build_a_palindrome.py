from suffix_tree import SuffixTree

if __name__ == '__main__':
    s1 = input()
    s2 = input()
    s2 = s2[::-1]
    tree1 = SuffixTree(s1)
    tree2 = SuffixTree(s2)
    print(tree1.nodes)
