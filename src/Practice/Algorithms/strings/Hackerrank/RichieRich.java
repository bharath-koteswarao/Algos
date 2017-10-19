package Algorithms.strings.Hackerrank;

import java.util.Scanner;

/**
 * Created by BK on 19-10-2017.
 */
public class RichieRich {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int len = sc.nextInt();
        int max = sc.nextInt();
        String inp = sc.next();
        int required = 0;
        for (int i = 0; i < Math.floorDiv(inp.length(), 2); i++) {
            if (inp.charAt(i) != inp.charAt(len - i - 1)) required += 1;
        }
        if (required > max) {
            System.out.println(-1);
        } else if (required == max) {
            StringBuffer temp = new StringBuffer(inp);
            for (int i = 0; i < len; i++) {
                if (temp.charAt(i) != temp.charAt(len - i - 1)) {
                    int biggest = Math.max(Int(temp.charAt(i)), Int(temp.charAt(len - i - 1)));
                    temp.setCharAt(i, (biggest + "").charAt(0));
                    temp.setCharAt(len - i - 1, (biggest + "").charAt(0));
                }
            }
            System.out.println(temp.toString());
        } else {
            int extra = max - required;
            StringBuffer temp = new StringBuffer(inp);
            for (int i = 0; i < len; i++) {
                if (temp.charAt(i) != temp.charAt(len - i - 1)) {
                    int biggest = Math.max(Int(temp.charAt(i)), Int(temp.charAt(len - i - 1)));
                    temp.setCharAt(i, (biggest + "").charAt(0));
                    temp.setCharAt(len - i - 1, (biggest + "").charAt(0));
                }
            }
            System.out.println("ans "+temp.toString()+" "+extra);
            for (int i = 0; i < len; i++) {
                if (extra > 0) {
                    if (inp.charAt(i) != '9') {
                        temp.setCharAt(i, (9 + "").charAt(0));
                        temp.setCharAt(len - i - 1, (9 + "").charAt(0));
                    }
                    extra -= 1;
                }
            }
            System.out.println(temp.toString());
        }
    }

    private static int Int(char c) {
        return Integer.parseInt(c + "");
    }
}
