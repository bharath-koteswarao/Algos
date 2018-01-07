from math import gcd as g

if __name__ == '__main__':
    for _ in range(int(input().strip())):
        a, c, b, d = [int(i) for i in input().strip().split()]
        if abs(a - b - c + d) % g(d, b) == 0:
            print("YES")
        else:
            print("NO")
