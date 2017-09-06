package Codeforces;

import java.util.Scanner;

/**
 * Created by BK on 05-09-2017.
 */
public class CurriculumVitae {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] inp = new int[n];
        for (int i = 0; i < n; i++) {
            inp[i] = scanner.nextInt();
        }
        int startingZeros = 0, endingOnes = 0;
        String str = "", formed;
        for (int i : inp) str += i;
        formed = str + "";
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '0') {
                startingZeros++;
                formed = str.substring(i + 1);
            } else break;
        }
        str = formed + "";
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) == '1') {
                endingOnes++;
                formed = str.substring(0, i);
            } else break;
        }
        System.out.println(formed);
        System.out.println(startingZeros + " " + endingOnes);
        int sum = startingZeros + endingOnes, ones = 0, zeroes = 0;
        for (int i = 0; i < formed.length(); i++) {
            if (formed.charAt(i) == '0') zeroes++;
            else ones++;
        }
        System.out.println(zeroes + " " + ones);
        zeroes += sum;
        ones += sum;
        System.out.println(Math.max(zeroes, ones));
    }
}
