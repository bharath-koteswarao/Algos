def binary_search_iterative(arr, element):
    found = False
    while len(arr) > 0 and not found:
        middle = len(arr) // 2
        if arr[middle] is element:
            found = True
        else:
            if element > arr[middle]:
                arr = arr[middle + 1:]
            else:
                arr = arr[0:middle]
    return found


def binary_search_recursive(arr, element):
    if len(arr) is 0:
        return False
    else:
        middle = len(arr) // 2
        if arr[middle] is element:
            return True
        else:
            if element > arr[middle]:
                return binary_search_recursive(arr[middle + 1:], element)
            else:
                return binary_search_recursive(arr[:middle], element)
    pass


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    element = int(input("Enter element to search : "))
    answer_iterative = binary_search_iterative(arr, element)
    answer_recursive = binary_search_recursive(arr, element)
    print("Found" if answer_iterative else "Not found", "used iterative method")
    print("Found" if answer_recursive else "Not found", "used recursive method")


main()
