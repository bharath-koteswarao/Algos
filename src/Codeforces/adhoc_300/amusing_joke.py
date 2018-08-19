from collections import Counter

if __name__ == '__main__':
    c1 = Counter(input().strip())
    c2 = Counter(input().strip())
    c3 = Counter(input().strip())
    for x in c2:
        if x not in c1:
            c1[x] = c2[x]
        else:
            c1[x] += c2[x]
    print("YES" if c1 == c3 else "NO")
