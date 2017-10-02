if __name__ == '__main__':
    tc = int(input().strip())
    for i in range(tc):
        num = int(input().strip())
        first = (num - 1) // 3
        second = (num - 1) // 5
        third = (num - 1) // 15
        one = 3 * (first * (first + 1))
        print(one/2)
        print(one//2,one/2 == one//2)
        two = 5 * (second * (second + 1)) // 2
        three = 15 * (third * (third + 1)) // 2
        ans = (one + two - three)
        print(int(ans))
