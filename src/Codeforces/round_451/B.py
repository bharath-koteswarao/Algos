from math import gcd as g

if __name__ == '__main__':
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    if n % a == 0 or n % b == 0:
        print("YES")
        if n % a == 0:
            print(n // a, 0)
        else:
            print(n // b, 0)
    else:
        if n % g(a, b) == 0:
            print("YES")
            re = n % a
        else:
            print("NO")
