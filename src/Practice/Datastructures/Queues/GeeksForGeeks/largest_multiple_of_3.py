from collections import deque


def main():
    que1 = deque([])
    que2 = deque([])
    n = int(input())
    inp = input()
    nums = inp.split(" ")
    total = 0
    for i in range(0, len(nums)):
        nums[i] = int(nums[i])
    for i in range(0, n):
        if nums[i] % 3 is 1:
            que1.append(nums[i])
        elif nums[i] % 3 is 2:
            que2.append(nums[i])
        total += nums[i]
    amount_to_remove = total % 3

    que1 = deque(sorted(que1))
    que2 = deque(sorted(que2))
    nums = sorted(nums)

    if amount_to_remove is 0:
        pass
    elif amount_to_remove is 1:
        nums.remove(que1.popleft())
    elif amount_to_remove is 2:
        if len(que2) is 0:
            nums.remove(que1.popleft())
            nums.remove(que1.popleft())
        else:
            nums.remove(que2.popleft())
    answer = ""
    for i in reversed(nums):
        answer += str(i)
    print(answer)


main()
