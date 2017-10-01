from Graph import Graph

"""
Do this problem when I become comfortable with several graph algorithms

https://www.hackerrank.com/contests/university-codesprint-3/challenges/march-of-the-king/problem
"""

def show_board(mat):
    for i in mat:
        for j in i:
            print(j, end=" ")
        print()


def add_edge(graph, i, j):

    pass


def buildGraph(graph, board):
    for i in range(8):
        for j in range(8):
            if i-1 >= 0 and j-1>=0 and i+1<8 and j+1<8:
                add_edge()
    pass


if __name__ == '__main__':
    input()
    graph = Graph()
    word = input().strip()
    board = [[] for i in range(8)]
    for i in range(8):
        board[i] = list(input().strip())
    show_board(board)
    buildGraph(graph, board)
