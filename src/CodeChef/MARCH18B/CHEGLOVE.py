if __name__ == '__main__':
    for _ in range(int(input().strip())):
        n = int(input().strip())
        fingers = [int(__) for __ in input().strip().split()]
        gloves = [int(__) for __ in input().strip().split()]
        front = back = True
        for i in range(n):
            if fingers[i] > gloves[i]:
                front = False
                break
        gloves = gloves[::-1]
        for i in range(n):
            if fingers[i] > gloves[i]:
                back = False
                break
        if front and back:
            print("both")
        elif front:
            print("front")
        elif back:
            print("back")
        else:
            print("none")
