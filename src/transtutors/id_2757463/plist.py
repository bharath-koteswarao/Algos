# Reading k from input during run time
k = int(input().strip())
# Reading the input array
plist1 = [int(num) for num in input().strip().split()]
# Using the python slicing to slice the array at (k - 1) th index since lists have 0 based index
plist2 = plist1[k - 1:]
print(plist2)
