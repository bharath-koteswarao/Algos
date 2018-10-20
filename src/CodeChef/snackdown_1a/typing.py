if __name__ == '__main__':
    for __ in range(int(input().strip())):
        n = int(input().strip())
        total = 0
        hand = {
            'd': 'l',
            'f': 'l',
            'j': 'r',
            'k': 'r'
        }
        finished = {}
        for _ in range(n):
            word = input().strip()
            if word in finished:
                total += finished[word] / 2
            else:
                cur = 2
                last = hand[word[0]]
                for i in range(1, len(word)):
                    if hand[word[i]] == last:
                        cur += 4
                    else:
                        cur += 2
                    last = hand[word[i]]
                finished[word] = cur
        print(int(total + sum(list(finished.values()))))
