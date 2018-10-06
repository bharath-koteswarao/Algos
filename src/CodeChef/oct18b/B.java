package CodeChef.oct18b;

import java.util.Scanner;

/**
 * Created by bk on 06-10-2018.
 */
public class B {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        long tc = sc.nextLong();
        while (tc-- > 0) {
            long n = sc.nextLong();
            long levels = 0;
            while (n > 26) {
                levels += 1;
                n -= 26;
            }
            long bits = (long) Math.pow(2, levels);
            long nib = 0;
            long bytes = 0;
            if (n > 10) {
                bytes = bits;
                bits = 0;
            } else if (n > 2) {
                nib = bits;
                bits = 0;
            } else if (n == 0) {
                bytes = bits;
                bits = 0;
            }
            System.out.println(bits + " " + nib + " " + bytes);
        }
    }
}
