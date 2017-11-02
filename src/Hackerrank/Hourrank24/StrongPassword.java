package Hackerrank.Hourrank24;

import java.util.Scanner;

public class StrongPassword {
    public static void main(String[] args) {
        String numbers = "0123456789";
        String lower_case = "abcdefghijklmnopqrstuvwxyz";
        String upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String special_characters = "!@#$%^&*()-+";
        boolean nums = false, low = false, up = false, sp = false;
        Scanner sc = new Scanner(System.in);
        sc.next();
        String inp = sc.next();
        int count = 0;
        for (int i = 0; i < inp.length(); i++) {
            if (numbers.contains(inp.charAt(i) + "") && !nums) {
                count += 1;
                nums = true;
            }
            if (lower_case.contains(inp.charAt(i) + "") && !low) {
                count += 1;
                low = true;
            }
            if (upper_case.contains(inp.charAt(i) + "") && !up) {
                count += 1;
                up = true;
            }
            if (special_characters.contains(inp.charAt(i) + "") && !sp) {
                count += 1;
                sp = true;
            }
        }
        if (inp.length() >= 8) {
            System.out.println(4 - count);
        } else {
            int temp = 4 - count;
            if (inp.length() + temp >= 6) {
                System.out.println(temp);
            } else {
                System.out.println(6 - (inp.length() + temp) + temp);
            }
        }
    }
}
