def divide(n, its, res, count):
    if n < its:
        n *= 10
        res.append(0)
    if count == its:
        return res
    else:
        res.append(n // its)
        return divide(n % its, its, res, count + 1)


if __name__ == '__main__':
    a, b, c = [int(__) for __ in input().strip().split()]
    arr = divide(a, b, [], 0)
    print(arr)
