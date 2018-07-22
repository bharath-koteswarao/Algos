# collecting space separated input from user and the length can be of any number
# Then converting that input string to array and then to int array
inp = [int(x) for x in input().strip().split()]
# sorting the input for making calculations easy
inp.sort()
# recent is used for traversing the input elements
recent = 0
for i in range(0, 100, 10):
    # This is the limit until which we have to check in each iteration
    limit = i + 10
    # Counting the number of elements that fall in this limit
    count = 0
    while recent < len(inp) and inp[recent] <= limit:
        count += 1
        recent += 1
    # ljust is used for creating neat spaces to the right side
    print(str(i + 1).ljust(3), '-'.ljust(3), str(i + 10).ljust(4), '|'.ljust(2), ('*' * count))
