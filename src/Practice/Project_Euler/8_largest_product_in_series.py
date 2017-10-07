"""
This solution has to be optimised
"""

if __name__ == '__main__':
    tc = int(input())
    for i_tc in range(tc):
        l, k = [int(i) for i in input().strip().split(" ")]
        nums = [int(i) for i in list(str(int(input().strip())))]
        mul_pos = []
        mul = 1
        for i in nums:
            mul *= i
            mul_pos.append(mul)
        print(mul_pos)
