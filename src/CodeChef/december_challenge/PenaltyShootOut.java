package CodeChef.december_challenge;

/*
 * Created by bk on 02-12-2017 12:37
 */

/*
10100101111011111111
00000000000000000000
01011101110110101111
10101110111001011111
*/

import java.io.BufferedInputStream;
import java.util.Scanner;

public class PenaltyShootOut {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(new BufferedInputStream(System.in));
        while (sc.hasNext()) {
            String s = sc.next();
            String a = "", b = "";
            for (int i = 0; i < s.length(); i++) {
                if (i % 2 == 0) a += s.charAt(i);
                else b += s.charAt(i);
            }
            boolean sudden = true;
            int f = 0, se = 0, diff, o1 = 0, o2 = 0;
            for (int i = 0; i < 5; i++) {
                if (a.charAt(i) == '1') o1 += 1;
                if (a.charAt(i) == '1') o2 += 1;
            }
            if (o1 == o2) {
                a = a.substring(5);
                b = b.substring(5);
                int count = 0;
                boolean found = false;
                for (int i = 0; i < a.length(); i++) {
                    count += 2;
                    if (a.charAt(i) == '1' && b.charAt(i) != '1') {
                        System.out.print("TEAM-A ");
                        found = true;
                        break;
                    } else if (a.charAt(i) != '1' && b.charAt(i) == '1') {
                        System.out.print("TEAM-Second ");
                        found = true;
                        break;
                    }
                }
                if (!found) System.out.println("TIE");
                else System.out.println(10 + count);
            } else {

            }
        }
    }
}
