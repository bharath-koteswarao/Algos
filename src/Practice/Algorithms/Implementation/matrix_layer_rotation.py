def get_numel(m, n, i):
    return 2 * (m + n - (2 ** (i + 1)) - 2)
# todo solve this without using brute force

if __name__ == '__main__':
    m, n, r = [int(i) for i in input().strip().split(" ")]
    layers = 1
    a, b = m, n
    while min((a, b)) != 2:
        (a, b) = (a - 2, b - 2)
        layers += 1
    lis = [[] for i in range(layers)]
    for i in range(layers):
        numel = get_numel(m, n, i)
