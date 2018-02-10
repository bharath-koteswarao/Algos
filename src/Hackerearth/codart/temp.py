from collections import Counter as cntr
from math import inf
def chk(cn):
    for i in cn:
        if cn[i]%4!=0:
            return False
    return True

a = input()
m = -inf
for l in range(4,len(a),4):
    for i in range(0,len(a)-l+1):
        temp = cntr(a[i:i+l])
        if chk(temp):
            m = max(m, l)
print(m)