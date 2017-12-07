from math import gcd

if __name__ == '__main__':
    tc = int(input().strip())
    a, b, c = [int(i) for i in input().strip().split(" ")]
    if gcd(a, gcd(b, c)) == 1:
        print("YES")
    else:
        print("NO")
