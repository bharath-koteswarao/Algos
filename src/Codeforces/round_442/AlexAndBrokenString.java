package Codeforces.round_442;

import java.util.Scanner;

public class AlexAndBrokenString {
    public final static int d = 256;


    public static void main(String[] z) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.next();
        String[] arr = {"Danil", "Olya", "Slava", "Ann", "Nikita"};
        int count = 0;
        for (int i = 0; i < arr.length; i++) {
            while (inp.contains(arr[i])) {
                count += 1;
                inp = inp.replaceFirst(arr[i], "");
            }
            if (count > 2) {
                break;
            }
        }
        System.out.println(count == 1 ? "YES" : "NO");
    }
}