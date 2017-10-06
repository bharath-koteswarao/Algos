if __name__ == '__main__':
    consonants = {
        'b': 1,
        'c': 1,
        'd': 1,
        'f': 1,
        'g': 1,
        'h': 1,
        'j': 1,
        'k': 1,
        'l': 1,
        'm': 1,
        'n': 1,
        'p': 1,
        'q': 1,
        'r': 1,
        's': 1,
        't': 1,
        'v': 1,
        'w': 1,
        'x': 1,
        'y': 1,
        'z': 1
    }
    positions = {}
    tc = int(input())
    for i_tc in range(tc):
        answer = ""
        word, length = input().strip().split(" ")
        length = int(length)
        vowels = 0
        cons = 0
        for i in range(len(word)):
            if word[i] in consonants:
                cons += 1
            else:
                vowels += 1
            positions[i] = [vowels, cons]
        front = -1
        answer = ""
        for i in range(length - 1,len(word)):
            if front >= 0:
                first = positions[i][0]-positions[front][0]
                second = positions[i][1] - positions[front][1]
                prod = first * second
                answer += str(prod)
                pass
            else:
                first = positions[i][0]
                second = positions[i][1]
                prod = first * second
                answer += str(prod)
            front += 1
        print(answer)
