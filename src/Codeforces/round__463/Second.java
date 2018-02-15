package Codeforces.round__463;

/*
 * Created by bk on 15-02-2018 21:18
 */

public class Second {
    private static long f(long n) {
        long pr = 1;
        while (n > 0) {
            long re = n % 10;
            if (re > 0) pr *= re;
            n = n / 10;
        }
        return pr;
    }

}
