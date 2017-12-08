from math import ceil as c

if __name__ == '__main__':
    tc = int(input().strip())
    for _ in range(tc):
        n = int(input().strip())
        arr = [int(i) for i in input().strip().split(" ")]
        while True:
            sm = min(arr)
            d = arr.index(sm) + 1
            de = []
            if sm == 0:
                for i in range(len(arr)):
                    arr[i] -= 1
                    if arr[i] < 0:
                        de.append(i)
            else:
                n = c((sm + d) / sm)
                r = -n * d
                for i in range(len(arr)):
                    arr[i] += r
                    if arr[i] < 0:
                        de.append(i)
            co = 0
            for i in de:
                del arr[i - co]
                co += 1
            if len(arr) == 1:
                print("Ladia")
                break
            elif len(arr) == 0:
                print("Kushagra")
                break
