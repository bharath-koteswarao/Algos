if __name__ == '__main__':
    s = input().strip()
    while True:
        co = 0
        if '21' in s:
            s = s.replace('21', '12')
            co += 1
        if '10' in s:
            s = s.replace('10', '01')
            co += 1
        if co == 0:
            break
    print(s)
