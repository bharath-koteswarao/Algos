package Sorting;

import Datastructures.bk;

/**
 * Created by bk on 30-08-2018.
 */
public class BubbleSort {
    public static void main(String[] __) {
        int[] unsorted = {1, 2, 3, 6, 5, 4};
//        bk.print_int(unsorted);
        bubbleSort(unsorted);
//        bk.print_int(unsorted);
    }

    private static void bubbleSort(int[] unsorted) {
        int len = unsorted.length;
        for (int i = 0; i < len; i++) {
            boolean req = false;
            bk.print_int(unsorted);
            for (int j = 0; j < len - i - 1; j++) {
                if (unsorted[j] > unsorted[j + 1]) {
                    int temp = unsorted[j];
                    unsorted[j] = unsorted[j + 1];
                    unsorted[j + 1] = temp;
                    req = true;
                }
            }
            if (!req) break;
        }
    }
}
