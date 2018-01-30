package Codeforces.round_459;

import java.util.Scanner;

public class C {
    public static void main(String[] __) {
        Scanner sc = new Scanner(System.in);
        String inp = sc.next();
        int ans = 0;
        for (int i = 0; i < inp.length(); i++) {
            int score = 0, qmarks = 0;
            for (int j = i; j < inp.length(); j++) {
                if (inp.charAt(j) == '(') score += 1;
                else if (inp.charAt(j) == ')') score -= 1;
                else {
                    if (qmarks >= score) score += 1;
                    else qmarks += 1;
                }
                if (score < 0) break;
                else if ((j - i) % 2 == 1) {
                    if (score == 0 && qmarks == 0) ans += 1;
                    else if (qmarks >= score) ans += 1;
                }
            }
        }
        System.out.println(ans);
    }
}