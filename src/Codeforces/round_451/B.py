from math import gcd as g

if __name__ == '__main__':
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    if n % g(a, b) == 0 and n >= max(a, b):
        print("YES")
        x, y = 0, 0
        if a > b:
            x = n // a
            n = n % a
            if n % b == 0:
                y = n // b
            else:
                x -= 1
                n += a
                y = n // b
            print(x,y)
        else:
            x = n // b
            n = n % b
            if n % a == 0:
                y = n // a
            else:
                x -= 1
                n += b
                y = n // a
            print(y,x)
    else:
        print("NO")
