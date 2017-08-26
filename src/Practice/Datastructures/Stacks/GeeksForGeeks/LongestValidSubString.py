tc = int(input())
while tc > 0:
    inp = input()
    l = []
    count = 0
    for i in inp:
        if i == '(' or i == '{' or i == '[':
            l.append(i)
        elif i == ')' and len(l) != 0:
            if l.pop() == '(':
                count += 2
        elif i == ']' and len(l) != 0:
            if l.pop() == '[':
                count += 2
        elif i == '}' and len(l) != 0:
            if l.pop() == '{':
                count += 2
    print(count)
    tc -= 1
