package Spoj;

import java.util.Scanner;

import static java.lang.Integer.parseInt;

/**
 * Created by BK on 16-10-2017.
 */
class Spoj42 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for(int i = 0;i<tc;i++) {
            int n1 = sc.nextInt();
            int n2 = sc.nextInt();
            System.out.println(
                    parseInt(
                            new StringBuffer(
                                    (parseInt(new StringBuffer(n1 + "").reverse().toString()) +
                                            parseInt(new StringBuffer(n2 + "").reverse().toString())) + ""
                            ).reverse().toString()
                    )
            );
        }
    }
}
