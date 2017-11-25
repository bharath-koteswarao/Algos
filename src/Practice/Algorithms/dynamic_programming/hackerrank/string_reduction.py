"""
3
cab
bcab
ccccc

Sample Output
2
1
5
"""

if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        inp = list(input().strip())
        if len(set(inp)) == 1:
            print(len(inp))
        else:
            memo = {'a': 0,
                    'b': 0,
                    'c': 0}
            for i in inp:
                memo[i] += 1
            if memo['a'] % 2 == 0 and memo['b'] % 2 == 0 and memo['c'] % 2 == 0:
                print(2)
            elif memo['a'] % 2 == 1 and memo['b'] % 2 == 1 and memo['c'] % 2 == 1:
                print(2)
            else:
                print(1)
