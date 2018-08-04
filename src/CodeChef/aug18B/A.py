from collections import Counter as c
def permute(i, top, bot, ans):
    if i != 3:
        permute(i + 1, top, bot, ans + top[i])
        permute(i + 1, top, bot, ans + bot[i])
    else:
        words.append(c(ans))


if __name__ == '__main__':
    for _ in range(int(input().strip())):
        top = list(input().strip())
        bot = list(input().strip())
        words = []
        permute(0, top, bot, "")
        found = False
        for i in words:
            if i['b'] == 2 and i['o'] == 1:
                found = True
                break
        print('yes' if found else 'no')
