class kcomp:
    arr = []
    su = 0
    start = 0
    end = 0

    def __init__(self, arr, su):
        self.arr = arr
        self.su = su
        self.start = 0
        self.end = len(self.arr) - 1

    def check(self, x):
        new = []
        for p in range(len(self.arr)):
            new.append(self.arr[p])
        return sum(new) <= self.su

    def ans(self):
        mid = (self.start + self.end) // 2
        while self.start <= self.end:
            if self.check(mid):
                self.start = mid + 1
            else:
                self.end = mid - 1
            mid = (self.start + self.end) // 2
        return self.start if self.check(self.start) else self.start - 1


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, k = [int(__) for __ in input().strip().split()]
        arr = [int(__) for __ in input().strip().split()]
        kc = kcomp(arr, k)
        print(kc.ans())
