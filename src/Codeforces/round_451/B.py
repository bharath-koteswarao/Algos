from math import gcd as g

if __name__ == '__main__':
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    if n % g(a, b) == 0 and n >= max(a, b):
        print("YES")
        i = 0
        found = False
        while True:
            y = (n - a * i) / b
            if y == int(y) and y > 0:
                found = True
                break
            else:
                i += 1
            if a * i > n:
                break
        if found:
            print(i, int(n - a * i) // b)
        else:
            i = 0
            while True:
                y = (n - b * i) / a
                if y == int(y) and y > 0:
                    break
                else:
                    i += 1
            print(int(n - a * i) // a, i)
    else:
        print("NO")
