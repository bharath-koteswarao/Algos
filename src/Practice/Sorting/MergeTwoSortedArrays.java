package Sorting;

import Datastructures.bk;

/**
 * Created by BK on 10-09-2017.
 */
public class MergeTwoSortedArrays {
    public static void main(String... z) {
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = {10, 20, 30, 40, 50, 60};
        int[] sorted = new int[arr1.length + arr2.length];
        for (int i = 0, j = 0, k = 0; k < sorted.length; k++) {
            if (i < arr1.length && j < arr2.length) {
                if (arr1[i] > arr2[j]) {
                    sorted[k] = arr1[i];
                    i++;
                } else {
                    sorted[k] = arr2[j];
                    j++;
                }
            } else {
                if (i >= arr1.length) {
                    sorted[k] = arr2[j];
                    j++;
                } else if (j >= arr2.length) {
                    sorted[k] = arr1[i];
                    i++;
                }
            }
        }
        bk.print_int(sorted);
    }
}
