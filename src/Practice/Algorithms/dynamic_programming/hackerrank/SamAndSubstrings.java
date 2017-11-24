package Algorithms.dynamic_programming.hackerrank;

/*
 * Created by bk on 24-11-2017 17:04
 */

import java.util.Scanner;

public class SamAndSubstrings {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.next();
        int end = 0, sum = 0;
        for (int i = 0; i < inp.length(); i++) {
            for (int j = 0; j < inp.length() - end; j++) {
                sum += Integer.parseInt(inp.substring(j, j + end + 1));
            }
            end += 1;
        }
        System.out.println(sum % 1000000007);
    }
}
