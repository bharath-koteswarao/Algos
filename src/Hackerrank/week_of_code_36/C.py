"""
1
########
B##P##k#
########
########
########
########
#K######
########
"""
if __name__ == '__main__':
    for _ in range(int(input().strip())):
        board = []
        for __ in range(8):
            board.append(list(input().strip()))
        wq, wn, wb, wr, wp = [], [], [], [], []
        black_king = None
        discovered = False
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'Q':
                    wq.append((i, j))
                    wr.append((i, j))
                    wb.append((i, j))
                elif board[i][j] == 'N':
                    wn.append((i, j))
                elif board[i][j] == 'Second':
                    wb.append((i, j))
                elif board[i][j] == 'R':
                    wr.append((i, j))
                elif board[i][j] == 'P':
                    wp.append((i, j))
                elif board[i][j] == 'k':
                    black_king = (i, j)
        tp = None
        for i in range(8):
            if board[1][i] == 'P' and board[0][i] == '#':
                tp = (0, i)
                board[1][i] = '#'
                break
        for i in wr:
            cur = i
            found = True
            if black_king[0] == cur[0]:
                if cur[1] > black_king[1]:
                    for j in range(cur[1] - 1, black_king[1], -1):
                        if board[cur[0]][j] != '#':
                            found = False
                            break
                else:
                    for j in range(cur[1] + 1, black_king[1]):
                        if board[cur[0]][j] != '#':
                            found = False
                            break
            else:
                found = False
            if found:
                discovered = True
        for i in wb:
            cur_x, cur_y = i
            bx, by = black_king
            found = True
            if abs(bx - cur_x) == abs(by - cur_y):
                if cur_x < bx and cur_y < by:
                    cur_x += 1
                    cur_y += 1
                    while cur_x < bx and cur_y < by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x += 1
                        cur_y += 1
                elif cur_x < bx and cur_y > by:
                    cur_x += 1
                    cur_y -= 1
                    while cur_x < bx and cur_y > by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x += 1
                        cur_y -= 1
                elif cur_x > bx and cur_y > by:
                    cur_x -= 1
                    cur_y -= 1
                    while cur_x > bx and cur_y > by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x -= 1
                        cur_y -= 1
                else:
                    cur_x -= 1
                    cur_y += 1
                    while cur_x > bx and cur_y < by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x -= 1
                        cur_y += 1
            else:
                found = False
            if found:
                discovered = True
        if discovered:
            print(4)
        else:
            ans = 0
            cur = tp
            found = True
            if black_king[0] == cur[0]:
                if cur[1] > black_king[1]:
                    for j in range(cur[1] - 1, black_king[1], -1):
                        if board[cur[0]][j] != '#':
                            found = False
                            break
                else:
                    for j in range(cur[1] + 1, black_king[1]):
                        if board[cur[0]][j] != '#':
                            found = False
                            break
            elif black_king[1] == cur[1]:
                for j in range(cur[0] + 1, black_king[1]):
                    if board[j][cur[1]] != '#':
                        found = False
                        break
            else:
                found = False
            if found:
                ans += 2
            cur_x, cur_y = tp
            bx, by = black_king
            found = True
            if abs(bx - cur_x) == abs(by - cur_y):
                if cur_x < bx and cur_y < by:
                    cur_x += 1
                    cur_y += 1
                    while cur_x < bx and cur_y < by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x += 1
                        cur_y += 1
                elif cur_x < bx and cur_y > by:
                    cur_x += 1
                    cur_y -= 1
                    while cur_x < bx and cur_y > by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x += 1
                        cur_y -= 1
                elif cur_x > bx and cur_y > by:
                    cur_x -= 1
                    cur_y -= 1
                    while cur_x > bx and cur_y > by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x -= 1
                        cur_y -= 1
                else:
                    cur_x -= 1
                    cur_y += 1
                    while cur_x > bx and cur_y < by:
                        if board[cur_x][cur_y] != '#':
                            found = False
                            break
                        cur_x -= 1
                        cur_y += 1
            else:
                found = False
            if found:
                ans += 2
            cur_x, cur_y = tp
            if (cur_x + 2, cur_y - 1) == black_king:
                ans += 1
            elif (cur_x + 1, cur_y - 2) == black_king:
                ans += 1
            elif (cur_x - 2, cur_y - 1) == black_king:
                ans += 1
            elif (cur_x - 1, cur_y - 2) == black_king:
                ans += 1
            elif (cur_x - 2, cur_y + 1) == black_king:
                ans += 1
            elif (cur_x - 1, cur_y + 2) == black_king:
                ans += 1
            elif (cur_x + 2, cur_y + 1) == black_king:
                ans += 1
            elif (cur_x + 1, cur_y + 2) == black_king:
                ans += 1
            print(ans)
