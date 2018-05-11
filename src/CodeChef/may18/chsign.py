"""
4
4
4 3 1 2
6
1 2 2 1 3 1
5
10 1 2 10 5
4
1 2 1 2

Example Output

4 3 -1 2
-1 2 2 -1 3 -1
10 -1 2 10 -5
1 2 -1 2

"""


class Solution:
    slots = []
    ans = None
    min_sum = None
    arr = None

    def __init__(self, arr, slots):
        self.slots = slots
        self.min_sum = sum(arr)
        self.ans = arr
        self.arr = arr
        self.get_ans(0, {}, arr, self.min_sum)
        self.prnt()

    def get_ans(self, idx, blocks, array, su):
        # print(array)
        if su < self.min_sum and self.validate(array):
            self.ans = array
            self.min_sum = su
        if idx < len(array):
            if self.slots[idx]:
                self.get_ans(idx + 1, blocks, array, su)
                temp = array[:]
                temp[idx] *= -1
                su -= abs(temp[idx] * 2)
                self.get_ans(idx + 1, blocks, temp, su)
            else:
                self.get_ans(idx + 1, blocks, array, su)

    def validate(self, array):
        for i in range(len(array)):
            if i < 2:
                try:
                    s1 = array[i] + array[i + 1] + array[i + 2]
                    if s1 <= 0:
                        return False
                except IndexError:
                    pass
            elif i >= len(array) - 2:
                try:
                    s2 = array[i] + array[i - 1] + array[i - 2]
                    if s2 <= 0:
                        return False
                except IndexError:
                    pass
            else:
                try:
                    s1 = array[i] + array[i + 1] + array[i + 2]
                    s2 = array[i] + array[i - 1] + array[i - 2]
                    if s1 <= 0 or s2 <= 0:
                        return False
                except IndexError:
                    pass
        return True

    def prnt(self):
        for i in self.ans:
            print(i, end=" ")
        print()


def get_slots(arr):
    slots = []
    for i in range(n):
        if i == 0:
            slots.append(1 if arr[i] < arr[i + 1] else 0)
        elif i == n - 1:
            slots.append(1 if arr[i] < arr[i - 1] else 0)
        else:
            slots.append(1 if (arr[i] < arr[i + 1] and arr[i] < arr[i - 1]) else 0)
    return slots


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = [int(__) for __ in input().strip().split()]
        if n == 2:
            if arr[0] == arr[1]:
                print(arr[0], arr[1])
            elif arr[0] < arr[1]:
                print(-arr[0], arr[1])
            elif arr[0] > arr[1]:
                print(arr[0], -arr[1])
        else:
            sol = Solution(arr, get_slots(arr))
