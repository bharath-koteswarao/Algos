from pprint import pprint as pp


def c(n, r, memo):
    r = r if r < (n - r) else (n - r)
    if (n, r) in memo:
        # print("Got ", (n, r), "from memo")
        return memo[(n, r)]
    elif n == r or r == 0:
        memo[(n, r)] = 1
        # print("Added",(n,r),"to memo")
        return 1
    elif r == 1 or (n - r == 1):
        memo[(n, r)] = n
        # print("Added",(n,r),"to memo")
        return n
    else:
        # print("calculated", (n, r))
        memo[(n, r)] = c(n - 1, r, memo) + c(n - 1, r - 1, memo)
        return memo[(n, r)]


def bottom_up_c(n, r, memo):
    for i in range(0, n+1):
        for j in range(0, r + 1):
            if n - r == 1 or r == 1:
                memo[(n, r)] = n
                memo[(n, n - r)] = n
            elif n == r or r == 0:
                memo[(n, r)] = 1
                memo[(n, n - r)] = 1
            else:
                memo[(n, r)] = memo[(n - 1, r - 1)] + memo[(n - 1, r)]
                memo[(n, n - r)] = memo[(n - 1, r - 1)] + memo[(n - 1, r)]
    return memo


if __name__ == '__main__':
    tc = int(input().split(" ")[0])
    for i in range(tc):
        (num1, num2) = [int(j) for j in input().split(" ")]
        memo = {
            (1, 0): 1,
            (1, 1): 1
        }
        answer = c(num1, num2, memo) % ((10 ** 9) + 7)
        ans2 = bottom_up_c(num1, num2, memo)
        print(answer)
    pp(memo)
    pp(ans2[(num1, num2)] % ((10 ** 9) + 7))
