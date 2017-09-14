def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    print("arr is ", arr, " left is ", left, " right is ", right)
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1
    print("merged is ",arr)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        """
        At each stage we take the array and split into left half and right half
        
        At that stage itself we merge it by the principle of merging two sorted halves
        
        So by end of that recursion stage the half ( either left or right ) becomes sorted
        
        """

        merge(arr, left, right)


def main():
    unsorted = [3, 463, 435, 46, 39, 9, 2, 1]
    print(unsorted)
    merge_sort(unsorted)
    print(unsorted)


main()
