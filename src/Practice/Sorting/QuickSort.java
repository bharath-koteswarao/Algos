package Sorting;

import Datastructures.bk;

/**
 * Created by bk on 30-08-2018.
 */
public class QuickSort {
    public static void main(String[] __) {
        int[] unsorted = {1, 2, 5, 4, 3};
        bk.print_int(unsorted);
        quickSort(0, unsorted.length - 1, unsorted);
        bk.print_int(unsorted);
    }

    private static void quickSort(int start, int end, int[] unsorted) {
        bk.print_int(unsorted);
        if (start < end) {
            int pivot = partition(start, end, unsorted);
            quickSort(start, pivot - 1, unsorted);
            quickSort(pivot + 1, end, unsorted);
        }
    }

    private static int partition(int start, int end, int[] arr) {
        int p1 = start - 1, p2 = start;
        while (p2 < end) {
            if (arr[p2] < arr[end]) {
                p1 += 1;
                int temp = arr[p1];
                arr[p1] = arr[p2];
                arr[p2] = temp;
            }
            p2 += 1;
        }
        p1 += 1;
        int temp = arr[p1];
        arr[p1] = arr[end];
        arr[end] = temp;
        return p1;
    }
}
