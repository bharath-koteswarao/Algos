package Datastructures.Stacks.GeeksForGeeks;

import java.util.Scanner;

/**
 * Created by BK on 08-08-2017.
 */

public class MinimumBracketReversals {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int tc = sc.nextInt();
        for (int k = 0; k < tc; k++) {
            String input = sc.next();
            int count = 0;
            if (input.length() % 2 != 0) {
                System.out.println(-1);
            } else {
                while (input.contains("{}")) {
                    input = input.replace("{}", "");
                }
                for (int i = 0; i < input.length(); i++) {
                    if (i % 2 == 0) {
                        count = input.charAt(i) == '{' ? count : count + 1;
                    } else {
                        count = input.charAt(i) == '}' ? count : count + 1;
                    }
                }
                System.out.println(count);
            }
        }
    }
}
