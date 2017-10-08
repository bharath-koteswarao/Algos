if __name__ == '__main__':
    tc = int(input())
    for i_tc in range(tc):
        inp = input().strip()
        strings = []
        if len(inp) == 0 or inp[0] == '0':
            print("NO")
        else:
            for i in range(0, len(inp) - 1):
                strings.append(inp[0:i + 1])
            found_answer = False
            for s in strings:
                temp = inp
                ans = s
                while temp.startswith(s):
                    temp = temp[len(s):]
                    s = str(int(s) + 1)
                if temp == "":
                    print("YES", ans)
                    found_answer = True
                    break
            if not found_answer:
                print("NO")
