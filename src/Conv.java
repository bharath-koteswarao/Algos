import Datastructures.bk;

import java.util.Arrays;

/**
 * Created by BK on 13-09-2017.
 */
public class Conv {
    public static void main(String[] args) {
        int[] x = {1, 2, -1, 0, 0, 0, 0};
        int[] h = {4, 1, 2, 5, 0, 0, 0};
        int[] y = new int[6];
        Arrays.fill(y, 0);
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < h.length; j++) {
                if (i - j >= 0)y[i] += x[i] * h[i - j];
            }
        }
        bk.print_int(y);
    }
}
