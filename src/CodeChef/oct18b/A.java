package CodeChef.oct18b;

import java.util.Scanner;

/**
 * Created by bk on 05-10-2018.
 */
public class A {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        while (tc-- > 0) {
            int a = sc.nextInt(), b = sc.nextInt(), k = sc.nextInt();
            int changes = (a + b) / k;
            System.out.println(changes % 2 == 0 ? "CHEF" : "COOK");
        }
    }
}
