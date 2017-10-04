def is_palindrome(number):
    length = len(number)
    for i in range(length // 2):
        if number[i] != number[length - 1 - i]:
            return False
    return True


if __name__ == '__main__':
    nums = [False for i in range(0, 1000000)]
    checked = {}
    for i in range(100, 1000):
        for j in range(100, 1000):
            mul = i * j
            if is_palindrome(str(mul)):
                nums[mul] = True
    tc = int(input())
    for tc_i in range(tc):
        for i in range(int(input()) - 1, 0, -1):
            if nums[i]:
                print(i)
                break
