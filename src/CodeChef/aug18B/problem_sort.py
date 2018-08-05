class Problem:
    diff = 0
    idx = 0

    lis = []

    def __init__(self, lis, idx):
        self.lis = lis
        self.idx = idx

    def __repr__(self):
        return str(self.lis)


if __name__ == '__main__':
    n, k = [int(__) for __ in input().strip().split()]
    problems = []
    for _ in range(n):
        l = []
        a = [int(__) for __ in input().strip().split()]
        b = [int(__) for __ in input().strip().split()]
        for p in range(k):
            l.append([a[p], b[p]])
        l.sort(key=lambda x: x[0])
        problems.append(Problem(l, _ + 1))

    for problem in problems:
        dif = 0
        for i in range(k - 1):
            if problem.lis[i][1] > problem.lis[i + 1][1]:
                dif += 1
        problem.diff = dif

    problems.sort(key=lambda x: (x.diff, x.idx))
    for problem in problems:
        print(problem.idx)
