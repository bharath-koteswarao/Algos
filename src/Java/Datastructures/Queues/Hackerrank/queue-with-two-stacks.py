stack1 = []
stack2 = []


def enqueue(n):
    stack1.append(n)


def transfer_all_to_stack2():
    while len(stack1) is not 0:
        stack2.append(stack1.pop())


def dequeue():
    if len(stack2) <= 0:
        transfer_all_to_stack2()
    stack2.pop()


def show():
    if len(stack2) <= 0:
        transfer_all_to_stack2()
    print(stack2[-1])


tc = int(input())
for i in range(0, tc):
    temp = list(map(int, input().split(' ')))
    n = temp[0]
    if n == 1:
        enqueue(temp[1])
    elif n is 2:
        dequeue()
    else:
        show()
