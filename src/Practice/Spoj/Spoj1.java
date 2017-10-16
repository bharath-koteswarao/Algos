package Spoj;

import java.util.Scanner;

/**
 * Created by BK on 16-10-2017.
 */
class Spoj1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int num = sc.nextInt();
            if(num == 42) System.exit(0);
            else System.out.println(num);
        }
    }
}
