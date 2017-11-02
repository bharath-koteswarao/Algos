if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        a, b, x = [int(i) for i in input().strip().split(" ")]
        ans = []
        for i in range(a, b + 1):
            count = 0
            for j in range(a, b + 1):
                if i != j:
                    if j % i != 0:
                        count += 1
            if count == b - a and len(ans) <= x:
                ans.append(i)
            if len(ans) >= x:
                break
        if len(ans) < x:
            print(-1)
        else:
            for p in ans:
                print(p, end=" ")
    print()
