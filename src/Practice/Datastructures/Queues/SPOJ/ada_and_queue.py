from collections import deque


def main():
    tc = int(input())
    q = deque([])
    toggle = False
    for i in range(0, tc):
        flag = input().split(" ")
        if flag[0] == "front":
            if len(q) == 0:
                print("No job for Ada?")
            else:
                if not toggle:
                    print(q.popleft())
                else:
                    print(q.pop())
        elif flag[0] == "back":
            if len(q) == 0:
                print("No job for Ada?")
            else:
                if not toggle:
                    print(q.pop())
                else:
                    print(q.popleft())
        elif flag[0] == "reverse":
            toggle = not toggle
        elif flag[0] == "toFront":
            if not toggle:
                q.appendleft(flag[1])
            else:
                q.append(flag[1])
        elif flag[0] == "push_back":
            if not toggle:
                q.append(flag[1])
            else:
                q.appendleft(flag[1])


main()
