from bisect import bisect_left as bs


def merge(arr, left, right):
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if abs(left[i] - num) < abs(right[j] - num):
            arr[k] = left[i]
            i += 1
        elif abs(left[i] - num) == abs(right[j] - num):
            if left[i] > right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
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
        # print("merged is ", arr)


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


if __name__ == '__main__':
    n, num = [int(i) for i in input().strip().split(" ")]
    arr = [int(i) for i in input().strip().split(" ")]
    ind = bs(arr, num, 0, len(arr))
    if ind == len(arr):
        for i in range(1, 6):
            print(arr[-i], end=" ")
    elif arr[ind] == num:
        if ind == 0:
            for i in range(4, -1, -1):
                print(i, end=" ")
        elif ind == n - 1:
            for i in range(1, 6):
                print(arr[-i], end=" ")
        else:
            temp = [arr[ind], arr[ind + 1], arr[ind + 2], arr[ind - 1], arr[ind - 2]]
            merge_sort(temp)
            for i in temp:
                print(i, end=" ")
        pass
    elif ind == 0:
        for i in range(4, -1, -1):
            print(i, end=" ")
