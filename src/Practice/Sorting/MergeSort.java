package Sorting;

import Datastructures.bk;

/**
 * Created by BK on 11-09-2017.
 */
public class MergeSort {
    static MergeTwoSortedArrays merge;

    public static void main(String[] args) {
        merge = new MergeTwoSortedArrays();
        int[] input = {4, 2, 12, 3, 13, 7, 1};
        bk.print_int(input);
        int[] sorted = mergeSort(input);
        bk.print_int(sorted);
    }

    public static int[] mergeSort(int[] input) {
        int[] sorted = new int[0];
        int[] left = leftArray(input, input.length / 2);
        int[] right = rightArray(input, left.length);
        if (left.length!=1){
            mergeSort(left);
        } else {
            System.out.print("Left : ");
            bk.print_int(left);
            System.out.print("Right : ");
            bk.print_int(right);
        }
        if (right.length!=1){
            mergeSort(right);
        }
        return sorted;
    }

    private static int[] rightArray(int[] input, int from) {
        int[] temp = new int[input.length - from];
        for (int i = 0; i < temp.length; i++) temp[i] = input[from + i];
//        System.out.print("Right : ");
//        bk.print_int(temp);
        return temp;
    }

    private static int[] leftArray(int[] input, int len) {
        int[] temp = new int[len];
        for (int i = 0; i < temp.length; i++) temp[i] = input[i];
//        System.out.print("Left : ");
//        bk.print_int(temp);
        return temp;
    }
}
