if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n, m = [int(__) for __ in input().strip().split()]
        invalid, weak = False, False
        for test in range(n):
            status, st = input().strip().split()
            fail = st.count('0')
            if status == 'correct':
                if fail != 0:
                    invalid = True
            if status == 'wrong':
                if fail == 0:
                    weak = True
        if invalid:
            print('INVALID')
        elif weak:
            print("WEAK")
        else:
            print("FINE")
