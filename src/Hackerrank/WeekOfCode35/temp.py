from fractions import Fraction as Fr


def bernoulli(n):
    print(n)
    A = [0] * (n + 1)
    for m in range(n + 1):
        A[m] = Fr(1, m + 1)
        for j in range(m, 0, -1):
            A[j - 1] = j * (A[j - 1] - A[j])
    return A[0]  # (which is Bn)


bn = []
for i in range(800,810):
    if i % 2 == 0:
        bn.append((i, bernoulli(i)))
    else:
        bn.append((i, 0))
bn = [(i, b) for i, b in bn]
s = ""
for i, b in bn:
    if i % 2 == 0:
        s += (str(i) + ":" + str(b.numerator) + "/" + str(b.denominator) + ",")
f = open("file.txt", 'w')
f.write(s)
f.close()
print("done")
