"""
ID: koteswa1
LANG: PYTHON2
TASK: test
"""
fin = open('test.in', 'r')
fout = open('test.out', 'w')
x, y = map(int, fin.readline().split())
total = x + y
fout.write(str(total) + '\n')
fout.close()
